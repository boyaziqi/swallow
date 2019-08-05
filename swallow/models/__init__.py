from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from swallow import App


db = SQLAlchemy(App)
migrate = Migrate(App, db)


def init_database():
    import swallow.models.uesrs
    db.create_all()
