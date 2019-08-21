import os

from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config = True)

    print('cc')
    @app.route('/health/check')
    def check():
        return 'It works!'

    return app
