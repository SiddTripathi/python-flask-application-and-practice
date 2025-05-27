from flask import Flask, request
from db import stores,items
from flask_smorest import abort
import uuid

app = Flask(__name__)




#get all stores
@app.get("/store")
def get_stores():
    return {"stores":list(stores.values())}


@app.post("/store")
def create_store(): 
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


@app.post("/item")
def create_item():                     #This is a dynamic route. The <string:name> part is a variable that will be passed to the function as an argument and header in URL
    item_data = request.get_json()
    if(
        "price" not in item_data or "store_id" not in item_data
        or "name" not in item_data 
    ):
        abort(400,message="Bad Request !!. Ensure 'price', 'store_id', and 'name' are included in JSON payload",)
    for item in items.values():
        if(item_data["name"] == item["name"]):
            abort(400,message="Item already exist",)
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found",)
    item_id = uuid.uuid4().hex
    item = {**item_data,"id":item_id}
    items[item_id] = item
    return item,201

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


#get store by name
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found",)

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found",)
