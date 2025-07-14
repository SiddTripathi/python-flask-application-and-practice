
import os
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from .blocklist import BLOCKLIST
from flask_smorest import Api
from .db import db
#from .models import StoreModel, ItemModel
from .resources.item import blp as ItemBlueprint
from .resources.store import blp as StoreBlueprint
from .resources.tag import blp as TagBlueprint
from .resources.users import blp as UserBlueprint


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
    migrate = Migrate(app,db)
    api = Api(app) #connects flask smorest extension with flask app
    app.config["JWT_SECRET_KEY"] = "83895029357195414167268476135934579751"
    jwt = JWTManager(app)

    """
`claims` are data we choose to attach to each jwt payload
and for each jwt protected endpoint, we can retrieve these claims via `get_jwt_claims()`
one possible use case for claims are access level control, which is shown below
"""
    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        print("IDENTITY IN CLAIMS LOADER:", identity, type(identity))
        if str(identity) == "1":
            return{"is_admin": True}
        return{"is_admin": False}

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header,jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header,jwt_payload):
        return(
            jsonify(
                {"description": "The token has been revoked","error": "token_revoked"}
            ),401
        )

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message":"The Token has expired","error":"token_expired"}),401,
        )
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return(
            jsonify({"message":"Signature verification failed","error":"invalid_token"}),401,
        )
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return(
            jsonify({"message":"Request does not contain access token","error":"authorization_required"}),401,
        )
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return(
            jsonify({

            
                "description":"The token is not fresh",
                "error":"Fresh token required"
            })
        )

    # with app.app_context():  # Ensures that all tables are created in the database if they do not already exist when the app starts. Note: It does not update existing tables; migrations are required for schema changes.
    #     db.create_all()              #commenting this as SQLAlchemy is no longer needed because of migrate databse

    

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)
    return app