DEBUG = True

USER = 'postgres'
PASSWORD = '123'
SERVER = 'localhost'
DB = 'flask_api'

SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True