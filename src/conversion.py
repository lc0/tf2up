"""Module to work on conversion / download related things"""

import logging
import os
import requests
import shutil
import subprocess

from hashlib import md5
from typing import Tuple, List


from flask import render_template
from storage import FileStorage


class NotebookDownloadException(Exception):
    """Notebook download exception"""

    def __init__(self, message):
        super(NotebookDownloadException, self).__init__(message)
        self.message = message

class ConvertionException(Exception):
    """NBdime conversion exception"""

    def __init__(self, message, details):
        super(ConvertionException, self).__init__(message)

        self.message = message
        self.details = details



def _download_file(requested_url: str) -> str:
    """Download a file from github repository"""

    url = f"https://github.com/{requested_url.replace('blob', 'raw')}"
    resp = requests.get(url)
    logging.info(F"Requested URL: {requested_url}")

    if resp.status_code != 200:
        logging.info(f"Can not download {url}")
        raise NotebookDownloadException("Can not download the file. Please, check the URL")

    return resp.text


# TODO: Run conversion in temp folder,
# so we do not have issues with concurrent conversion
def _convert_file(in_file: str, out_file: str) -> List[str]:
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


def _save_ipynb_from_py(folder: str, py_filename: str) -> str:
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
        file_content = _download_file(file_url)

        os.mkdir(path)
        with open(f"{path}/{original}", "w") as original_file:
            original_file.write(file_content)

        try:
            output = _convert_file(f"{path}/{original}", f"{path}/{converted}")
        except ConvertionException as error:
            shutil.rmtree(path)
            raise error

        with open(f"{path}/output", "w") as summary_output:
            summary_output.write('\n'.join(output))

        shutil.copy('report.txt', f"{path}/report")

        # persist `report.txt` to GCS
        storage = FileStorage()
        storage.save_file('report.txt', folder_hash)

        # found a python file, need to encode separately
        if original.endswith('.py'):
            result_filenames = []
            for py_file in [original, converted]:
                result_filenames.append(_save_ipynb_from_py(path, py_file))

            assert len(result_filenames) == 2
            return path, tuple(result_filenames[:2])

    if original.endswith('.py'):
        return path, (original.replace('.py', '.ipynb'),
                      converted.replace('.py', '.ipynb'))

    return path, (original, converted)


def inject_nbdime(content: str, folder_hash: str, tf_version: str) -> str:
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

    # TODO: separate flask from inject function
    return render_template("nbdime_inject.html",
                           before=content[:position],
                           report_lines=report_lines,
                           after=content[position:],
                           folder=folder_hash,
                           file='converted.ipynb',
                           tf_version=tf_version)