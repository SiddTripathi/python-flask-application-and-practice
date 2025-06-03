import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from ..schemas import ItemSchema, ItemUpdateSchema
from ..db import stores,items



blp = Blueprint("items",__name__, description="Operations on items")

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

        #return {"items": list(items.values())}   --> this is replaced by marshmallow response method returning multiple items in Schema
        # The mashmallow returns a list instead of object

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self,item_data):
        for item in items.values():
            if(item_data["name"] == item["name"]):
                abort(400,message="Item already exist",)
        if item_data["store_id"] not in stores:
            abort(404, message="Store not found",)
        item_id = uuid.uuid4().hex
        item = {**item_data,"id":item_id}
        items[item_id] = item
        return item,201


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self,item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)              #keep in mind that order of decorators matter. Best practice to keep response deco nested deeper compared to argument
    def update(self,item_data,item_id):
        item_data = request.get_json()

        #this below is more optimised way
        try:
             item = items[item_id]
             item |= item_data
             return item
        except KeyError:
            abort(404,message="Item not found")
        # for item in items.values():
        #     if(item_data["name"] == item["name"]):
        #         abort(400,message="Item already exist",)  --> this is also one of the way to do it
        # item = {**item_data,"id":item_id}
        # items[item_id] = item
        # return item,201
    
    
    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message":"Item has been deleted"}
        except KeyError:
            abort(404, message="Item not found")