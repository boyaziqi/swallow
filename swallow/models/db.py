from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app import App


database_config = App.config.get('DATABASE')
if not database_config:
    raise Exception("dont't set database config info")

engine = create_engine(
    f'mysql+mysqldb://{database_config["user"]}:{database_config["password"]}@'
    f'{database_config["host"]}:{database_config["port"]}/{database_config["db_name"]}'
    f'?charset={database_config["charset"]}'
    ,
    convert_unicode=True,
)
db_session = scoped_session(
    sessionmaker(autocommit=False,autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import swallow.models.uesrs

    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
