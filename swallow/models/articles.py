from sqlalchemy import Column, Integer, String, DateTime

from swallow.db import db


class Article(db.Model):
    """
    文章 model
    """
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False, default='')
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f'<Article {self.title}>'


class Category(db.Model):
    """
    文章分类 model
    """
    __tablename__ = 'article_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)


class Tag(db.Model):
    """
    文章标签 model
    """
    __tablename__ = 'article_tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
