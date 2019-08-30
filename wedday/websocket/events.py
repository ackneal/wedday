from flask import Blueprint
from flask_socketio import emit
from .. import socketio

bp = Blueprint("ws", __name__)

@socketio.on('new')
def new(data):
    emit('new', data, json=True, broadcast=True, include_self=False)
