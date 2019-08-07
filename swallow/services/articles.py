from swallow.db import db

from swallow.models.articles import Article
from swallow.models.articles import Category
from swallow.models.articles import Tag


def add_article(info):
    article = Article(**info)
    db.session.add(article)
    db.session.commit()


def update_article(article, info):
    article.title = info['title']
    article.content = info['content']
    db.session.add(article)
    db.session.commit()
