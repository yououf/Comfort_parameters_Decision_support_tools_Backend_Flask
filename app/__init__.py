from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

from app.utils import CustomJSONEncoder

db = SQLAlchemy()
migrate = Migrate()
mongo = PyMongo()


# application factory
def create_app(config):
    # create application instance
    app = Flask(__name__)
    app.config.from_object(config)
    app.json_encoder = CustomJSONEncoder

    db.init_app(app)
    migrate.init_app(app, db)
    mongo.init_app(app)


    # register blueprints
    from patient import patients_blueprint
    from pressure import pressure_blueprint
    from authentification import authentification_blueprint
    from region import regions_blueprint
    from mask import masks_blueprint
    from humidifier import humidifiers_blueprint
    from sensor import sensors_blueprint
    from environmental_data import environmental_data_blueprint
    from humidifier_quiz_questions import quiz_humidifier_questions_blueprint
    from technician import technicians_blueprint
    from comfort_questions import comfort_feedback_questions_blueprint
    from comfort import comforts_blueprint

    app.register_blueprint(patients_blueprint)
    app.register_blueprint(pressure_blueprint)
    app.register_blueprint(authentification_blueprint)
    app.register_blueprint(regions_blueprint)
    app.register_blueprint(masks_blueprint)
    app.register_blueprint(humidifiers_blueprint)
    app.register_blueprint(sensors_blueprint)
    app.register_blueprint(environmental_data_blueprint)
    app.register_blueprint(sensors_blueprint)
    app.register_blueprint(environmental_data_blueprint)
    app.register_blueprint(quiz_humidifier_questions_blueprint)
    app.register_blueprint(technicians_blueprint)
    app.register_blueprint(comfort_feedback_questions_blueprint)
    app.register_blueprint(comforts_blueprint)
    return app
