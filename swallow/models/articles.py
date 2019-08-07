from swallow.db import db


article_tag_rls = db.Table(
    'article_tags_rls',
    db.Column(
        'article_id', db.Integer, db.ForeignKey('articles.id'),
        primary_key=True,
    ),
    db.Column(
        'tag_id', db.Integer, db.ForeignKey('article_tags.id'),
        primary_key=True,
    ),
)

class Article(db.Model):
    """
    文章 model
    """
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False, default='')
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    category_id = db.Column(
        db.Integer, db.ForeignKey('article_categories.id'), nullable=False,
    )
    tags = db.relationship(
        'Tag',
        secondary=article_tag_rls,
        backref=db.backref('articles', lazy=True),
        lazy='subquery',
    )
    comments = db.relationship('Comment', backref='article', lazy=True)

    def __repr__(self):
        return f'<Article {self.title}>'


class Category(db.Model):
    """
    文章分类 model
    """
    __tablename__ = 'article_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    articles = db.relationship('Article', backref='category', lazy=True)


class Tag(db.Model):
    """
    文章标签 model
    """
    __tablename__ = 'article_tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
