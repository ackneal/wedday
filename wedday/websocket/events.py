from flask import Blueprint
from flask_socketio import emit
from .. import socketio

bp = Blueprint("ws", __name__)

@socketio.on('new', namespace='/ws')
def new(data):
    emit('new', data, json=True)
