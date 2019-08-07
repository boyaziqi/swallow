from swallow.db import db


class User(db.Model):
    """
    用户 modeg
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    mobile = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    nickname = db.Column(db.String(50), unique=True, nullable=False, default='')
    password = db.Column(db.String(50), nullable=False, default='')

    def __repr__(self):
        return f'<User {self.name}>'
