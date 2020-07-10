from flask import Flask, request
app = Flask(__name__)

from db import get_SELECT

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

@app.route('/aaa')
def aaa():
    a = request.args.get('name')
    return a

@app.route('/db')
def getdb():
    a = str(get_SELECT())
    return a

## おまじない
if __name__ == "__main__":
    app.run(debug=True)