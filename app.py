from flask import Flask 
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the main page <h1>HELLO!<h1>"

@app.route("/<name>")
def hello(name):
    # swapping escape(name) for x generates an alert. escape() is our security function
    # x = "<script>alert(\"uh oh, security breach\")</script>"
    return f"Hello, {escape(name)}!"

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == "__main__":
    app.run()