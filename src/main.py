"""Simple wrapper to upgrade the files by github URL"""

import json
import os
import subprocess
import urllib

from hashlib import md5
from typing import Tuple, List

import requests

from flask import Flask, redirect, request, render_template
app = Flask(__name__)

Summary = List[str]


def download_file(requested_url: str) -> str:
    """Download a file from github repository"""

    url = f"https://github.com/{requested_url.replace('blob', 'raw')}"
    resp = requests.get(url)
    print(requested_url)
    print(resp.status_code)

    if resp.status_code != 200:
        raise ValueError

    return resp.text


def convert_file(in_file: str, out_file: str) -> List[str]:
    """Upgrade file with tf_upgrade_v2."""

    comand = f"tf_upgrade_v2 --infile {in_file} --outfile {out_file}"

    p = subprocess.Popen(comand,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    result = p.stdout.readlines()
    p.wait()

    return result


def process_file(file_url: str, force=False) -> Tuple[str, Tuple[str, str], Summary]:
    """Process file with download, cache and upgrade."""

    _, file_ext = os.path.splitext(file_url)
    folder_hash = md5(file_url.encode('utf-8')).hexdigest()

    path = f"/notebooks/{folder_hash}"
    original = f"original{file_ext}"
    converted = f"converted{file_ext}"

    if not os.path.exists(path) or force:
        file_content = download_file(file_url)

        os.mkdir(path)
        with open(f"{path}/{original}", "w") as original_file:
            original_file.write(file_content)

        output = convert_file(f"{path}/{original}", f"{path}/{converted}")
        with open(f"{path}/output", "w") as summary_output:
            summary_output.write('\n'.join(output))

    else:
        with open(f"{path}/output") as summary_output:
            output = summary_output.readlines()

    return path, (original, converted), output


@app.route("/")
def hello():
    """Index page with intro info."""
    return render_template('index.html')


@app.route("/d/<path:path>", methods=['GET'])
def proxy(path):
    """Proxy request to index of `nbdime`"""

    nbdime_url = os.environ.get('NBDIME_URL')
    params = '&'.join([f"{k}={v}" for k, v in request.values.items()])
    url = f"{nbdime_url}{path}?{params}"

    print(f"URL: {url}")

    try:
        response = urllib.request.urlopen(url)
        return response.read()
    except urllib.error.URLError:
        return "Something went wrong, can not proxy"


@app.route("/d/<path:path>", methods=['POST'])
def proxy_api(path):
    """Proxy request to `nbdime` API"""

    nbdime_url = os.environ.get('NBDIME_URL')
    url = f"{nbdime_url}{path}"

    try:
        payload = json.dumps(request.json).encode()
        headers = {'content-type': 'application/json'}

        req = urllib.request.Request(url,
                                     data=payload,
                                     headers=headers)
        resp = urllib.request.urlopen(req)

        return resp.read()
    except urllib.error.URLError:
        return "Something went wrong, can not proxy"


# TODO force refresh
@app.route('/<path:path>')
def catch_all(path):
    """Endpoint for all URLs from Github"""

    # TODO: proper status codes
    if not (path.endswith('.py') or path.endswith('.ipynb')):
        return "Currently we only support `.py` and `.ipynb` files."

    try:
        folder, files, summary = process_file(path)

        if 'ERROR' in summary:
            print('='*10, 'ERROR!')
        for line in summary:
            print(line)

        url = f"/d/diff?base={folder}/{files[0]}&remote={folder}/{files[1]}"
        print(url)
        return redirect(url, code=302)

    except ValueError:
        return "Can not download the file :( Are you sure the URL is correct?"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
