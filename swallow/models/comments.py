from swallow.db import db

from swallow.models import articles


class Comment(db.Model):
    """
    文章 model
    """
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False, default='')
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    article_id = db.Column(
        db.Integer, db.ForeignKey('articles.id'), nullable=False,
    )
