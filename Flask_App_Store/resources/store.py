from sqlite3 import IntegrityError

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from models.stores import StoreModel
from sqlalchemy.exc import SQLAlchemyError

from db import db

from schemas import StoreSchema

blp = Blueprint("stores",__name__, description="Operations on stores")




@blp.route("/store")
class GetStore(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
        #return {"stores":list(stores.values())} --> refer items.py for this explanation
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self,store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Store with that name already exists")
        except SQLAlchemyError:
            abort(500,message="An error occured while creating a Store")
        return store

#<----------OLD CODE - Just for reference ---------->

"""
@blp.route("/store")
class GetStore(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()
        #return {"stores":list(stores.values())} --> refer items.py for this explanation
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self,store_data):
        #store_data = request.get_json() #the request converts json string to python dictionary. 
        # Request here is basically body which will be send along with get request. This is commented because now we are using marshmallow for data validation
        # and json request body
        for store in stores.values():
            if store_data["name"] == store["name"]:
                 abort(400, message="Store already exist. Try adding new name",)
    
        store_id = uuid.uuid4().hex
        new_store = {**store_data,"id":store_id}
        stores[store_id] = new_store
        return new_store,201

#One key think to note here - Lists cannot be used as database because they are not persistent. So if you restart the server, the data will be lost. 
# So we need to use a database to store the data. We can use SQLite or any other database to store the data. But for now, we will use a list to store the data. 
# In future, we will use a database to store the data.
"""
@blp.route("/store/<int:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message":"Store deleted successfully"}