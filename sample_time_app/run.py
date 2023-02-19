from flask import Flask
app = Flask(__name__)

import datetime

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    datetime_p = datetime.datetime.now()
    datetime_s = datetime.datetime.strftime(datetime_p, '%Y-%m-%d %H:%M:%S')
    return datetime_s

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
