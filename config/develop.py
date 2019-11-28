from config.base import *

DEBUG = True
ENV = 'development'

# DATABASE = {
#     'host' : '127.0.0.1',
#     'port': 3306,
#     'db_name': 'swallow',
#     'user': 'root',
#     'password': 'docker_mysql',
#     'charset': 'utf8mb4',
# }

SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://root:yLKGHEZ+haja6Nnboa5KygoDeA=@127.0.0.1/swallow?charset=utf8mb4'
