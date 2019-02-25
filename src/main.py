"""Simple wrapper to upgrade the files by github URL"""

import os

import requests

from hashlib import md5
from flask import Flask
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
    path = f"/tmp/tft/{folder_hash}"

    if not os.path.exists(path):
        file_content = download_file(requested_url)

        os.mkdir(path)
        with open(f"{path}/original{file_ext}", "w") as original_file:
            original_file.write(file_content)

        # TODO: try to convert



@app.route("/")
def hello():
    return "Hello World!"

# TODO force refresh
@app.route('/<path:path>')
def catch_all(path):

    # TODO: proper status codes
    if not (path.endswith('.py') or path.endswith('.ipynb')):
        return "Currently we only support `.py` and `.ipynb` files."

    try:
        print(process_file(path))
        return f"Original path is : {path}"
    except ValueError:
        return "Can not download the file :( . Are you sure the url is correct?"



if __name__ == "__main__":
    # bjoern.run(app, 0, 80)
    app.run(debug=True, host="0.0.0.0")