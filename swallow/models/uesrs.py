from sqlalchemy import Column, Integer, String

from swallow.models import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(50), unique=True, nullable=False, default='')
    password = Column(String(50), unique=True, nullable=False, default='')

    def __repr__(self):
        return f'<User {self.name}>'
