from flask import Flask
import os

app = Flask(__name__)

ready = True
live = True

@app.route('/')
def hello():
    return f"""
    <h1>Hello world</h1>
    """

@app.route('/live/check')
def live_check():
    if live :
        return "live"
    else:
        return 'bad request!', 400

@app.route('/live/stop')
def live_stop():
    global live
    live = False
    return "OK"

@app.route('/live/start')
def live_start():
    global live
    live = True
    return "OK"

@app.route('/ready/check')
def ready_check():
    if ready :
        return "READY"
    else:
        return 'bad request!', 400

@app.route('/ready/stop')
def ready_stop():
    global ready
    ready = False
    return "OK"

@app.route('/ready/start')
def ready_start():
    global ready
    ready = True
    return "OK"

if __name__ == "__main__":
   app.run(host='0.0.0.0')
