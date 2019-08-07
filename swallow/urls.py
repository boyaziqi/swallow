from flask import Blueprint
from flask_restful import Api

from swallow.views.articles import ArticleListView
from swallow.views.articles import ArticleView
from swallow.views.articles import CategoryListView
from swallow.views.articles import CategoryView
from swallow.views.articles import TagListView
from swallow.views.articles import TagView


article_bp = Blueprint('articles', __name__)
article_api = Api(article_bp, prefix='/articles')

article_api.add_resource(ArticleListView, '/')
article_api.add_resource(ArticleView, '/<int:article_id>')
article_api.add_resource(CategoryListView, '/categories')
article_api.add_resource(CategoryView, '/categories/<int:category_id>')
article_api.add_resource(TagListView, '/tags')
article_api.add_resource(TagView, '/tags/<int:tag_id>')
