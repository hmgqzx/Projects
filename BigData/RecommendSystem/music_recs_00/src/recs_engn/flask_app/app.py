from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    # resolve parameters of the request:
    # http://127.0.0.1:5050/?itemId=aba32456oeutpraoneucc&userId=ao1235123ec&type=old&ip=127.0.0.1
    item_id = request.args.get('itemId', '')
    user_id = request.args.get('userId', '')
    action_type = request.args.get('type', '')
    ip = request.args.get('ip', '')
    string = item_id + ' ' + user_id + ' ' + action_type + ' ' + ip
    return string


app.run(host='127.0.0.1', port='5050', debug=True)
