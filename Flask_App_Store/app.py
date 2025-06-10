
import os
from flask import Flask
from flask_smorest import Api
from .db import db
from .models import StoreModel, ItemModel
from .resources.item import blp as ItemBlueprint
from .resources.store import blp as StoreBlueprint


def create_app(db_url=None):
    instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "instance") #--> this ensures folder is created inside current working dir
    app = Flask(__name__, instance_path=instance_path)




    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] ="3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"]  = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")  #connection string for sqlite to connect with app (client). 
                                                                                           #This will create data.db file storing our data. The OS.getenv,
                                                                                           # will use value of DATABASE_URL or default to sqllite...)

    db.init_app(app) #initialises sqlalchemy extension passing in our flask app so that sql alchemy can connect with it
    api = Api(app) #connects flask smorest extension with flask app
    with app.app_context():  # Ensures that all tables are created in the database if they do not already exist when the app starts. Note: It does not update existing tables; migrations are required for schema changes.
        db.create_all()

    

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    return app