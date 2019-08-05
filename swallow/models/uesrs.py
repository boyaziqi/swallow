from sqlalchemy import Column, Integer, String

from swallow.db import db


class User(db.Model):
    """
    用户 modeg
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(50), unique=True, nullable=False, default='')
    password = Column(String(50), unique=True, nullable=False, default='')

    def __repr__(self):
        return f'<User {self.name}>'
