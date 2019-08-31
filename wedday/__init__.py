from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI = 'mysql://wedday:weddaysecret@127.0.0.1:3307/wedday',
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    db.init_app(app)

    from . import websocket, card
    app.register_blueprint(websocket.bp)
    app.register_blueprint(card.bp)
    socketio.init_app(app, cors_allowed_origins='*')

    @app.route('/')
    @app.route('/slide')
    def index():
        return render_template('index.html')

    return app
