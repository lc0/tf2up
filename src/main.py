from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    # bjoern.run(app, 0, 80)
    app.run(debug=True, host="0.0.0.0")