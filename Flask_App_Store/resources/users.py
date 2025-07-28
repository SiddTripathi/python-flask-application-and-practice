from sqlite3 import IntegrityError
import os
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, get_jwt,jwt_required, create_refresh_token, get_jwt_identity
import jwt
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from blocklist import BLOCKLIST

from models.user import UserModel
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import pbkdf2_sha256
from db import db

from schemas import UserSchema, UserRegisterSchema


blp = Blueprint("users",__name__, description="User management")



@blp.route("/user/<int:user_id>")
class GetUser(MethodView):
    @blp.response(200, UserSchema)
    def get(self,user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
    
    def delete(self, user_id):
        user = UserModel.query.get(user_id)
        if user is None:
            abort(400, message="User does not exist")
        db.session.delete(user)
        db.session.commit()

        return {"message":"User deleted successfuly"},200

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserRegisterSchema())
    def post(self,user_data):
        if UserModel.query.filter(UserModel.username==user_data["username"]).first():
            abort(409, message="Username has been taken, try a new one")
        user = UserModel(
            username=user_data["username"],
            email = user_data["email"],
            password = pbkdf2_sha256.hash(user_data["password"])
        )

        db.session.add(user)
        db.session.commit()
        message = Mail(
        from_email='siddharth.asbwork@gmail.com',
        to_emails=user.email,
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>User has been registered Test</strong>')
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            # sg.set_sendgrid_data_residency("eu")
            # uncomment the above line if you are sending mail using a regional EU subuser
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(str(e))

        return {"message": f"User {user.username} created successfully"}, 201

@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self,user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()
        print("this is user",user)
        if user and pbkdf2_sha256.verify(user_data["password"],user.password):
            print("LOGIN IDENTITY", user.id, type(user.id))
            access_token = create_access_token(identity=str(user.id),fresh=True)
            refresh_token = create_refresh_token(identity=str(user.id))
            return {"access_token": access_token,"refresh_token":refresh_token},200
        abort(401, message = "Unauthorized User")
@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True) 
    def post(self):
        current_user  = get_jwt_identity()
        new_token = create_access_token(identity=str(current_user),fresh=False)
        return {"access_token": new_token},200



@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required(fresh=True)
    @blp.arguments(UserSchema)
    def post(self,user_data):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message":"Successfully logged out"}