# from xml.etree.ElementTree import Comment
from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand

from app.models import Post,User,Comment,Like

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Like=Like,Comment=Comment,Post=Post)

if __name__ == '__main__':
    manager.run()