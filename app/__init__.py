from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from config import config_options

db = SQLAlchemy()
blog = "database.db"


def create_app(config_name):
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = "helloworld"
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{blog}'
   
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth/")

    from .models import User, Post, Comment, Like

    # create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists("app/" + blog):
        db.create_all(app=app)
        print("Created database!")