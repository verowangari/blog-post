from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from config import config_options

db = SQLAlchemy()



def create_app(config_name):
    app = Flask(__name__)
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    # app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get('DATABASE_URL')
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    
      
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    from .models import User, Post, Comment, Like

    # create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


