"""Simple wrapper to upgrade the files by github URL"""

import json
import logging
import os
import re
import urllib

# TODO: install file properly with `pip install -e .`
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from conversion import inject_nbdime, process_file
from conversion import NotebookDownloadException, ConvertionException


import mistune
import tensorflow as tf


from flask import (
    Flask, redirect, request, render_template, send_from_directory)
app = Flask(__name__)


@app.route("/")
def hello():
    """Index page with intro info."""
    return render_template('index.html',
                           tf_version=tf.version.VERSION)


@app.route('/download/<string:folder>/<path:filename>')
def download(folder, filename):
    """Allow to download files."""

    # TODO: move all /notebooks to a single config
    uploads = os.path.join('/notebooks/', folder)
    return send_from_directory(directory=uploads, filename=filename)


@app.route('/pages/<string:page_path>')
def show_page(page_path):
    """Render custom pages like stats"""

    renderer = mistune.Renderer(escape=False)
    markdown = mistune.Markdown(renderer=renderer)

    pages_folder = os.environ.get('PAGES_PATH', 'src/pages')
    page_path = os.path.join(pages_folder, f"{page_path}.md")

    if os.path.exists(page_path):
        with open(page_path) as page:
            content = page.read()
            rendered_content = markdown(content)

            return render_template('page.html',
                                   content=rendered_content)
    else:
        return render_template('error.html',
                               message='Page not found',
                               details='Did you try to check other pages?'), 404


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
                content = inject_nbdime(content.decode('utf-8'),
                                        folder_hash,
                                        tf_version=tf.version.VERSION)
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
