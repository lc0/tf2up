"""Simple wrapper to upgrade the files by github URL"""

import json
import logging
import os
import re
import shutil
import subprocess
import urllib

from hashlib import md5
from typing import Tuple, List

import requests
import tensorflow as tf

from flask import (
    Flask, redirect, request, render_template, send_from_directory)
app = Flask(__name__)


class NotebookDownloadException(Exception):
    pass

class ConvertionException(Exception):

    def __init__(self, message, details):
        self.message = message
        self.details = details



def download_file(requested_url: str) -> str:
    """Download a file from github repository"""

    url = f"https://github.com/{requested_url.replace('blob', 'raw')}"
    resp = requests.get(url)
    logging.info(F"Requested URL: {requested_url}")

    if resp.status_code != 200:
        logging.info(f"Can not download {url}")
        raise NotebookDownloadException("Can not download the file. Please, check the URL")

    return resp.text


def convert_file(in_file: str, out_file: str) -> List[str]:
    """Upgrade file with tf_upgrade_v2."""

    comand = f"tf_upgrade_v2 --infile {in_file} --outfile {out_file}"

    process = subprocess.Popen(comand,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    result_bytes = process.stdout.readlines()
    process.wait()

    result = [line.decode('utf-8') for line in result_bytes]
    if process.returncode:
        details = "<br>".join(result)
        raise ConvertionException("Can not convert the file", details)

    return result

def save_ipynb_from_py(folder: str, py_filename: str) -> str:
    """Save ipynb file based on python file"""

    full_filename = f"{folder}/{py_filename}"
    with open(full_filename) as pyfile:
        code_lines = [line.replace("\n", "\\n").replace('"', '\\"')
                      for line in pyfile.readlines()]
        pycode = '",\n"'.join(code_lines)

    with open('template.ipynb') as template:
        template_body = ''.join(template.readlines())

    ipynb_code = template_body.replace('{{TEMPLATE}}', pycode)

    new_filename = full_filename.replace('.py', '.ipynb')
    with open(new_filename, "w") as ipynb_file:
        ipynb_file.write(ipynb_code)

    return py_filename.replace('.py', '.ipynb')


def process_file(file_url: str) -> Tuple[str, Tuple[str, ...]]:
    """Process file with download, cache and upgrade."""

    _, file_ext = os.path.splitext(file_url)
    folder_hash = md5(file_url.encode('utf-8')).hexdigest()

    path = f"/notebooks/{folder_hash}"
    original = f"original{file_ext}"
    converted = f"converted{file_ext}"

    # TODO: delete the folder completely if `force`
    if not os.path.exists(path):
        file_content = download_file(file_url)

        os.mkdir(path)
        with open(f"{path}/{original}", "w") as original_file:
            original_file.write(file_content)

        try:
            output = convert_file(f"{path}/{original}", f"{path}/{converted}")
        except ConvertionException as error:
            shutil.rmtree(path)
            raise error

        with open(f"{path}/output", "w") as summary_output:
            summary_output.write('\n'.join(output))

        shutil.copy('report.txt', f"{path}/report")

        # found a python file, need to encode separately
        if original.endswith('.py'):
            result_filenames = []
            for py_file in [original, converted]:
                result_filenames.append(save_ipynb_from_py(path, py_file))

            assert len(result_filenames) == 2
            return path, tuple(result_filenames[:2])

    if original.endswith('.py'):
        return path, (original.replace('.py', '.ipynb'),
                      converted.replace('.py', '.ipynb'))

    return path, (original, converted)


def inject_nbdime(content: str, folder_hash: str) -> str:
    """Inject report strings before `nbdime`' diff"""
    replace_token = "<h3>Notebook Diff</h3>"
    position = content.find(replace_token)

    # nothing to inject here, just return the content
    if position == -1:
        return content

    path = f"/notebooks/{folder_hash}"
    with open(f"{path}/report") as summary_output:
        report_lines = [line for line in summary_output.readlines()
                        if line.strip() != '']

    return render_template("nbdime_inject.html",
                           before=content[:position],
                           report_lines=report_lines,
                           after=content[position:],
                           folder=folder_hash,
                           file='converted.ipynb',
                           tf_version=tf.version.VERSION)


@app.route("/")
def hello():
    """Index page with intro info."""
    return render_template('index.html',
                           tf_version=tf.version.VERSION)


@app.route('/download/<path:folder>/<path:filename>')
def download(folder, filename):
    """Allow to download files."""

    # TODO: move all /notebooks to a single config
    uploads = os.path.join('/notebooks/', folder)
    return send_from_directory(directory=uploads, filename=filename)


@app.route("/d/<path:path>", methods=['GET'])
def proxy(path):
    """Proxy request to index of `nbdime`"""

    nbdime_url = os.environ.get('NBDIME_URL')
    params = '&'.join([f"{k}={v}" for k, v in request.values.items()])
    url = f"{nbdime_url}{path}?{params}"

    logging.info(f"URL: {url}")

    try:
        response = urllib.request.urlopen(url)
        content = response.read()

        if b'notebooks' in content:
            folder_hash = re.findall(r"/notebooks\/([^\/]+)/", url)[0]

            try:
                content = inject_nbdime(content.decode('utf-8'), folder_hash)
                return content
            except FileNotFoundError:
                return ("The cache was invalidated meanwhile. "
                        "Please start by submitting the URL again.")

        else:
            return content

    except urllib.error.URLError:
        logging.error(f"Can not proxy nbdime for GET: {url}")
        message = "Something went wrong, can not proxy nbdime"
        return render_template('error.html', message=message), 502



@app.route("/d/<path:path>", methods=['POST'])
def proxy_api(path):
    """Proxy request to `nbdime` API"""

    nbdime_url = os.environ.get('NBDIME_URL')
    url = f"{nbdime_url}{path}"

    try:
        payload = json.dumps(request.json).encode()
        headers = {'content-type': 'application/json'}

        # dirty hack: seems like sometimes nbdime looses `content type`
        # from `application/json` to `text/plain;charset=UTF-8`
        if not request.json:
            logging.warning(f"WARNING: somehow lost json payload {request.json}")

            base = re.findall(r"base=([^\&]+)", request.referrer)[0]
            remote = re.findall(r"remote=([^\&]+)", request.referrer)[0]
            payload = json.dumps({'base': base, 'remote': remote})
            payload = payload.replace('%2F', '/').encode('utf-8')


        req = urllib.request.Request(url,
                                     data=payload,
                                     headers=headers)
        resp = urllib.request.urlopen(req)

        return resp.read()

    except urllib.error.URLError:
        logging.error(f"Can not proxy nbdime for POST: {url}")
        message = "Something went wrong, can not proxy nbdime"
        return render_template('error.html', message=message), 502


# TODO force refresh
@app.route('/<path:path>')
def catch_all(path):
    """Endpoint for all URLs from Github"""

    if not (path.endswith('.py') or path.endswith('.ipynb')):
        message = "Currently we only support `.py` and `.ipynb` files."
        return render_template('error.html', message=message), 501

    try:
        folder, files = process_file(path)

        url = f"/d/diff?base={folder}/{files[0]}&remote={folder}/{files[1]}"
        return redirect(url, code=302)

    except NotebookDownloadException as error:
        message = error.args[0]
        return render_template('error.html', message=message), 400

    except ConvertionException as error:
        logging.error(f"Can not convert for path {path}: {error.details}")
        return render_template('error.html',
                               message=error.message,
                               details=error.details), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
