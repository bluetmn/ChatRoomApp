from flask import Flask, render_template, request, url_for
from flask_socketio import SocketIO, emit, join_room
import os

app = Flask(__name__)
set_key = os.urandom(32)
app.config(SECRET_KEY) = set_key
SIO = SocketIO(app)
SIO.init_app(app)
