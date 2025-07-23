from flask_jwt_extended import get_jwt, jwt_required

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from models.items import ItemModel
from db import db


from ..schemas import ItemSchema, ItemUpdateSchema




blp = Blueprint("items",__name__, description="Operations on items")

@blp.route("/item")
class ItemList(MethodView):
    @jwt_required(fresh=True)
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

        #return {"items": list(items.values())}   --> this is replaced by marshmallow response method returning multiple items in Schema
        # The mashmallow returns a list instead of object
    @jwt_required(fresh=True)
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self,item_data):
        
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the data")

        return item,201


@blp.route("/item/<int:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)              #keep in mind that order of decorators matter. Best practice to keep response deco nested deeper compared to argument
    def update(self,item_data,item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(**item_data)    #store id needs to be passed if creating a item which does not exist. Check the updateItemSchema. Store_id there is not a 
                                            #required field
        db.session.add(item)
        db.session.commit()
        return item
    @jwt_required(fresh=True)
    def delete(self,item_id):
        jwt = get_jwt()
        print(get_jwt())
        if not jwt.get("is_admin", False):
            abort(401, message="Admin permissions needed")
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message":"Item has been deleted successfully"}