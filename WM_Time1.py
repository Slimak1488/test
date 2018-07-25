
from flask import Flask, render_template, request, url_for, redirect, send_from_directory,jsonify
from werkzeug.utils import secure_filename
import datetime


app = Flask(__name__)


@app.route('/', methods=['GET'])
def clock():
    return render_template('clock.html')


@app.route("/time", methods=['GET'])
def get_time():
    return jsonify(datetime.datetime.now().strftime('%H'), datetime.datetime.now().strftime('%M'))

#ffff
app.run()
