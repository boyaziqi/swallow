from sqlalchemy import Column, Integer, String

from swallow.models.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'