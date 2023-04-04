from flask import Flask

app = Flask(__name__)

# Hello world, mlb stats


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
