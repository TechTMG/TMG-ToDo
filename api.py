from flask import Flask, request
app = Flask(__name__)

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

## おまじない
if __name__ == "__main__":
    app.run(debug=True)