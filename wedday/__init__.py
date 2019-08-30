from flask import Flask, render_template
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)

    from . import websocket
    app.register_blueprint(websocket.bp)
    socketio.init_app(app, cors_allowed_origins='*')

    @app.route('/')
    @app.route('/slide')
    def index():
        return render_template('index.html')

    return app
