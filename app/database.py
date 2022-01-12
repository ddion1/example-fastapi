from os import get_inheritable
from pydantic import env_settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
#import psycopg2
#from psycopg2.extras import RealDictCursor
#import time

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@localhost:5432/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocale = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocale()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost',database='fastapi', user='postgres',
#         password='password', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successfull!")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("Error ", error)
#         time.sleep(2)

#cur = conn.cursor()
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
#cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
#cur.execute("SELECT * FROM fastapi;")
#cur.fetchone()
#conn.commit()
#cur.close()
#conn.close()

#cursor.close()
#conn.close()

# my_posts = [{"title": "title pf post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p


# on mac (environment variables)
# in cli : export MY_DB_URL="localhost:5432"
# 

# git 
# git ignore
# __pycache__
# venv/
# .env 