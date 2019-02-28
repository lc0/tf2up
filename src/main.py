"""Simple wrapper to upgrade the files by github URL"""

import json
import os
import urllib

import requests

from hashlib import md5
from flask import Flask, redirect, request
app = Flask(__name__)

def download_file(requested_url: str) -> str:
    """Download a file from github repository"""

    url = f"https://github.com/{requested_url.replace('blob', 'raw')}"
    resp = requests.get(url)
    print(requested_url)
    print(resp.status_code)

    if resp.status_code != 200:
        raise ValueError

    return resp.text

# TODO: return url
def process_file(requested_url: str, force=False):

    _, file_ext = os.path.splitext(requested_url)
    folder_hash = md5(requested_url.encode('utf-8')).hexdigest()
    path = f"/notebooks/{folder_hash}"

    if not os.path.exists(path):
        file_content = download_file(requested_url)

        os.mkdir(path)
        with open(f"{path}/original{file_ext}", "w") as original_file:
            original_file.write(file_content)

        # TODO: try to convert
        converted = f"converted{file_ext}"

    return path, (f"original{file_ext}", converted)



@app.route("/")
def hello():
    return "Hello World!"


@app.route("/d/<path:path>", methods=['GET'])
def proxy(path):
    """Proxy request on python side"""
    additional_params = '&'.join([f"{k}={v}" for k,v in request.values.items()])

    base = "http://127.0.0.1:52774/d/"
    # base = "http://localhost:81/d/"
    url = f"{base}{path}?{additional_params}"

    print(f"URL: {url}")

    try:
        response = urllib.request.urlopen(url)
        return response.read()
    except urllib.error.URLError:
        return "Something went wrong, can not proxy"


@app.route("/d/<path:path>", methods=['POST'])
def proxy_api(path):
    """Proxy request on python side"""
    # base = "http://127.0.0.1:52774/d/"
    base = "http://localhost:81/d/"
    url = f"{base}{path}"

    try:
        payload = json.dumps(request.json).encode()
        req =  urllib.request.Request(url, data=payload, headers={'content-type': 'application/json'}) # this will make the method "POST"
        resp = urllib.request.urlopen(req)

        return resp.read()
    except urllib.error.URLError:
        return "Something went wrong, can not proxy"

# TODO force refresh
@app.route('/<path:path>')
def catch_all(path):

    # TODO: proper status codes
    if not (path.endswith('.py') or path.endswith('.ipynb')):
        return "Currently we only support `.py` and `.ipynb` files."

    try:
        folder, files = process_file(path)

        url = f"/d/diff?base={folder}/{files[0]}&remote={folder}/{files[1]}"
        print(url)
        return redirect(url, code=302)

    except ValueError:
        return "Can not download the file :( . Are you sure the url is correct?"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")