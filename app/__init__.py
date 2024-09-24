

from flask import Flask
from config import Config

from .routes import create_routes



def get_environment_config():
    if Config.FLASK_ENV == "testing":
        return "config.TestingConfig"
    elif Config.FLASK_ENV == "production":
        return "config.ProductionConfig"
    else:
        return "config.DevelopmentConfig"



def create_app():

    app = Flask(__name__)

    # CORS(app, resources={r'/*': {'origins':'*'}})
    # getting the config environment
    CONFIG_TYPE = get_environment_config()
    app.config.from_object(CONFIG_TYPE)

    create_routes(app)
    # create_error_handler(app)
    return app

app = create_app()
