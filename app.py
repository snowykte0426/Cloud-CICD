from flask import Flask

app = Flask(__name__)


@app.route('/health')
def hello_world():
    return 'OK'

@app.route('/error')
def error():
    raise Exception('This is an error!')

if __name__ == '__main__':
    app.run()
