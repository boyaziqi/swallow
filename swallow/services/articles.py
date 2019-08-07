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


def add_category(info):
    category = Category(**info)
    db.session.add(category)
    db.session.commit()


def update_category(category, info):
    category.name = info['name']
    db.session.add(category)
    db.session.commit()


def add_tag(info):
    tag = Tag(**info)
    db.session.add(tag)
    db.session.commit()


def update_tag(tag, info):
    tag.name = info['name']
    db.session.add(tag)
    db.session.commit()
