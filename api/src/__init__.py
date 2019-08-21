import os

from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config = True)

    @app.route('/api/health/check')
    def check():
        return 'It works!'

    return app
