import os

from flask import Flask, render_template
from flask_sockets import Sockets

def create_app():
    app = Flask(__name__)
    sockets = Sockets(app)

    @sockets.route('/ws')
    def chat_socket(ws):
        while not ws.closed:
            message = ws.receive()
            if message is None:
                continue

            clients = ws.handler.server.clients.values()
            for client in clients:
                client.ws.send(message)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
