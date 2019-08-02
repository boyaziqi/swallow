from flask_sqlalchemy import SQLAlchemy

from swallow import App

db = SQLAlchemy(App)


def init_database():
    import swallow.models.uesrs
    db.create_all()
