import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SuperSecretKey')
    DATABASE_TYPE = os.environ.get('DATABASE_TYPE', 'mysql+pymysql')
    DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME', 'flaskuser')
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'flaskpassword')
    DATABASE_HOST = os.environ.get('DATABASE_HOST', '127.0.0.1')
    DATABASE_PORT = os.environ.get('DATABASE_PORT', '3306')
    DATABASE_NAME = os.environ.get('DATABASE_NAME', 'flaskapp')

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 
        f"{DATABASE_TYPE}://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False