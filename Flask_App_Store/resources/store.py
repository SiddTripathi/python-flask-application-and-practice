import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from ..db import stores

blp = Blueprint("stores",__name__, description="Operations on stores")




@blp.route("/store")
class GetStore(MethodView):
    def get(self):
        return {"stores":list(stores.values())}
    
    def post(self):
        store_data = request.get_json() #the request converts json string to python dictionary. Request here is basically body which will be send along with get request
        if "name" not in store_data:
            abort(400, message="Bad Request. 'name' should be present in JSON payload",)
    
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

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self,store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")


    def delete(self,store_id):
        try:
            del stores[store_id]
            return {"message":"Store has been deleted"}
        except KeyError:
            abort(404,message="Store not found")