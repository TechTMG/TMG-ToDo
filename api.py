from flask import Flask, request, jsonify
from db import get_alltask, get_task, post_task, update_task

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    title = "Tech TMG"
    return title


@app.route('/task', methods=['GET'])
def getalltask():
    get_json = get_alltask()
    if get_json:
        task_return = jsonify(get_json)
    else:
        task_return = jsonify({"message": "タスクデータはありません"})
    return task_return


@app.route('/task/<id>', methods=['GET'])
def gettask(id):
    get_json = get_task(id)
    if get_json:
        task_return = jsonify(get_json)
    else:
        task_return = jsonify({"message": "該当idのデータはありません"})
    return task_return


@app.route('/task', methods=['POST'])
def posttask():
    post_json = request.get_data()
    response = post_task(post_json)
    return response


@app.route('/task/<id>', methods=['POST'])
def updatetask():
    post_json = request.get_data()
    response = update_task(post_json)
    return response


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
