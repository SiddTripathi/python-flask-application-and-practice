from flask import Flask, request

app = Flask(__name__)


stores = [
    {
        "name":"My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]


#get all stores
@app.get("/store")

def get_stores():
    return {"stores":stores}


@app.post("/store")
def create_store():
    request_data = request.get_json() #the request converts json string to python dictionary. Request here is basically body which will be send along with get request
    new_store = {"name": request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store,201

#One key think to note here - Lists cannot be used as database because they are not persistent. So if you restart the server, the data will be lost. 
# So we need to use a database to store the data. We can use SQLite or any other database to store the data. But for now, we will use a list to store the data. 
# In future, we will use a database to store the data.


@app.post("/store/<string:name>/item")
def create_item(name):                     #This is a dynamic route. The <string:name> part is a variable that will be passed to the function as an argument and header in URL
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


#get store by name
@app.get("/store/<string:name>")
def get_store_by_name(name):
    for store in stores:
        if store["name"] == name:
            return store,200
    return {"message":"Store does not exist"},404

@app.get("/store/<string:name>/item")
def get_item_of_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items":store["items"]}           #best practice to return dictionary instead of list is because its easier to handle and manipulate dict(object)
    return {"message":"Store not found"},404
