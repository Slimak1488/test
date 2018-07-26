
from flask import Flask, render_template, request, url_for, redirect, send_from_directory,jsonify
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, emit, send
import socket
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketIO = SocketIO(app)


@app.route('/', methods=['GET'])
def clock():
    return render_template('clock.html')


@socketIO.on('connect')
def on_connect():
    send('connected', broadcast=True)


@socketIO.on('my_event')
def test_message():
    seconds_left = 60
    time_h = datetime.datetime.now().strftime('%H')
    time_m = datetime.datetime.now().strftime('%M')
    print("OK")
    emit('time', {'min': time_m, 'hour': time_h})


if __name__ == '__main__':
    socketIO.run(app)



