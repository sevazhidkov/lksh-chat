from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwaszxcx21312431231465843'
socketio = SocketIO(app)

from . import views
from . import events
from . import forms
