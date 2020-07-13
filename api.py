from flask import Flask, request, jsonify
from db import get_alltask, get_task

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


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


@app.route('/task', methods=['GET'])
def getalltask():
    a = get_alltask()
    if a:
        a = jsonify(a)
    else:
        a = jsonify({"message": "タスクデータはありません"})
    return a


@app.route('/task/<n>')
def gettask(n):
    a = get_task(n)
    if a:
        a = jsonify(a)
    else:
        a = jsonify({"message": "該当idのデータはありません"})
    return a


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
