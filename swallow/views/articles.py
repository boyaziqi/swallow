from flask_restful import Resource


class ArticleListView(Resource):
    def get(self):
        return {"test": "hello FanXu"}

    def post(self):
        pass


class ArticleView(Resource):
    def get(self, article_id):
        return f'article id is: {article_id}'

    def put(self):
        pass

    def delete(self):
        pass
