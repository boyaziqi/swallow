from flask import Blueprint
from flask_restful import Api

from swallow.views.articles import ArticleListView
from swallow.views.articles import ArticleView


article_bp = Blueprint('articles', __name__)
article_api = Api(article_bp, prefix='/articles')

article_api.add_resource(ArticleListView, '/')
article_api.add_resource(ArticleView, '/<int:article_id>')
