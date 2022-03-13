import os

class Config:


    SECRET_KEY ='SECRET_KEY'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','')
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', "postgresql://", 1)


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://vero:1234567890@localhost:5432/blog"
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}