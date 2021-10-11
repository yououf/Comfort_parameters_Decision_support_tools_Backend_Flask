from flask_migrate import MigrateCommand
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig
from app import create_app

from flask_script import Manager

app = create_app(DevelopmentConfig)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
jwt = JWTManager(app)



if __name__ == '__main__':
    manager.run()
