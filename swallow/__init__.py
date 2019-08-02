import os

from flask import Flask

from enviroment import SETTINGS_MODULE


def create_app(name=__name__):
    """
    创建应用

    :param test_config:
    :return:
    """
    app = Flask(name)

    app.config.from_object(SETTINGS_MODULE)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

App = create_app()