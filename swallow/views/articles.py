from flask_restful import fields
from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful import reqparse

from swallow.db import db
from swallow.models.articles import Article
from swallow.models.articles import Category
from swallow.models.articles import Tag
from swallow.services.articles import add_article
from swallow.services.articles import update_article
from swallow.services.articles import add_category
from swallow.services.articles import update_category
from swallow.services.articles import add_tag
from swallow.services.articles import update_tag


article_parse = reqparse.RequestParser()
article_parse.add_argument('title', type=str, required=True, help='标题')
article_parse.add_argument('content', type=str, required=True, help='内容')
article_parse.add_argument('category_id', type=int, required=True, help='分类id')


article_fields = {
    'title': fields.String,
    'content': fields.String,
    'created_at': fields.DateTime(dt_format='iso8601'),
    'updated_at': fields.DateTime(dt_format='iso8601'),
}


class ArticleListView(Resource):
    @marshal_with(article_fields, envelope='result')
    def get(self):
        article = Article.query.all()
        return article

    def post(self):
        args = article_parse.parse_args()
        add_article(args)

        return {'message': '成功'}

class ArticleView(Resource):
    @marshal_with(article_fields, envelope='result')
    def get(self, article_id):
        article = Article.query.filter_by(id=article_id).first_or_404()
        return article

    def put(self, article_id):
        article = Article.query.filter_by(id=article_id).first_or_404()
        args = article_parse.parse_args()
        update_article(article, args)

        return {'message': '成功'}

    def delete(self, article_id):
        article = Article.query.filter_by(id=article_id).first_or_404()
        db.session.delete(article)
        db.session.commit()


category_parse = reqparse.RequestParser()
category_parse.add_argument('name', type=str, required=True, help='名称')

category_fields = {
    'name': fields.String,
}


class CategoryListView(Resource):
    @marshal_with(category_fields, envelope='result')
    def get(self):
        return Category.query.all()

    def post(self):
        args = category_parse.parse_args()
        add_category(args)


class CategoryView(Resource):
    @marshal_with(category_fields, envelope='result')
    def get(self, category_id):
        return Category.query.filter_by(id=category_id).first_or_404()

    def put(self, category_id):
        category = Category.query.filter_by(id=category_id).first_or_404()
        update_category(category)

    def delete(self, category_id):
        category = Category.query.filter_by(id=category_id).first_or_404()
        db.session.delete(category)
        db.session.commit()


class TagListView(Resource):
    @marshal_with(category_fields, envelope='result')
    def get(self):
        return Tag.query.all()

    def post(self):
        args = category_parse.parse_args()
        add_tag(args)


class TagView(Resource):
    @marshal_with(category_fields, envelope='result')
    def get(self, tag_id):
        return Tag.query.filter_by(id=tag_id).first_or_404()

    def put(self, tag_id):
        tag = Tag.query.filter_by(id=tag_id).first_or_404()
        update_tag(tag)

    def delete(self, tag_id):
        tag = Tag.query.filter_by(id=tag_id).first_or_404()
        db.session.delete(tag)
        db.session.commit()
