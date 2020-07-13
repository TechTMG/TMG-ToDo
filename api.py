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
        task_return = jsonify(task_json)
    else:
        task_return = jsonify({"message": "タスクデータはありません"})
    return task_return


@app.route('/task/<n>', methods=['GET'])
def gettask(n):
    task_json = get_task(n)
    if task_json:
        task_return = jsonify(task_json)
    else:
        task_return = jsonify({"message": "該当idのデータはありません"})
    return task_return


@app.route('/task', methods=['POST'])
def posttask():
    post_json = request.get_data()
    post_task(post_json)
    complete = "COMPLETE"
    return complete


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
