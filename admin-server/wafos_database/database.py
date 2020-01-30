from rest_framework.views import APIView
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


# engine = create_engine('mysql+pymysql://root:wafos!@@175.126.37.210/wafos?charset=utf8', echo=False)
engine = create_engine('postgresql+psycopg2://wafos:wafos@localhost:5432/wafos', echo=False)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

conn = engine.connect()

def init_db():
    Base.metadata.create_all(engine)

