from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello, Flask'


app.run(host='127.0.0.1', port='5050', debug=True)
