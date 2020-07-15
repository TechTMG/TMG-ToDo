from flask import Flask, request, jsonify
from db import get_alltask, get_task, post_task

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    title = "Tech TMG"
    return title


@app.route('/task', methods=['GET'])
def getalltask():
    task_json = get_alltask()
    if task_json:
        result = jsonify(task_json)
    else:
        result = "タスクデータはありません"
    return result


@app.route('/task/<id>', methods=['GET'])
def gettask(id):
    task_json = get_task(id)
    if task_json:
        result = jsonify(task_json)
    else:
        result = "該当idのデータはありません"
    return result


@app.route('/task', methods=['POST'])
def posttask():
    post_json = request.get_data()
    return post_task(post_json)


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
