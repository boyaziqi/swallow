from flask import Flask

from enviroment import SETTINGS_MODULE
from flask_migrate import Migrate

from swallow.db import db
from swallow.models import uesrs, articles, comments
from swallow.urls import article_bp


def create_app(name=__name__):
    """
    创建应用

    :param test_config:
    :return:
    """
    app = Flask(name)

    app.config.from_object(SETTINGS_MODULE)
    # 绑定 SQLAlchemy 和当前 App
    db.init_app(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

app = create_app()
migrate = Migrate(app, db)

app.register_blueprint(article_bp)
# app.url_map.strict_slashes = False
