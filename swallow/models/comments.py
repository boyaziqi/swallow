from sqlalchemy import Column, Integer, String, DateTime


from swallow.db import db


class Comment(db.Model):
    """
    文章 model
    """
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    content = Column(String(300), nullable=False, default='')
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
