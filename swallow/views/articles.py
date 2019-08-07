from flask_restful import fields
from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful import reqparse

from swallow.db import db
from swallow.models.articles import Article
from swallow.services.articles import add_article
from swallow.services.articles import update_article


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
