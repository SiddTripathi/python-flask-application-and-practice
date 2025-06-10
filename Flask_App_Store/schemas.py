from marshmallow import Schema, fields




#this item schema does not deals with stores at all. Just fetches item related information
class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True) #dump_only means that it cannot be part of send request but only be generated and returned
    name = fields.Str(required=True) #data validation
    price=fields.Float(required=True)
    


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True,load_only=True) #this schema can be used to pass store id in request to fetch item details about the items of that store
    store = fields.Nested(PlainStoreSchema(),dump_only=True) #only used when returning the data of nested store within item

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()),dump_only=True)
       


#########  SIMPLE EXPLANATION OF WHY WE USE PLAIN SCHEMA ######################
# class ItemSchema(PlainItemSchema):
#     store_id = fields.Int(required=True, load_only=True)
#     store = fields.Nested(PlainStoreSchema(), dump_only=True)
# This code is used to add extra fields to the item schema.
#
# Particularly, fields.Nested means that it will add the fields corresponding to the PlainStoreSchema.
#
# dumply_only means that it will only add these fields when we dump (return) the schema in a POST request for example.
#
# Here is an example output of an item dump:
#
# {
#     "id": 1,
#     "name": "item name",
#     "price": 13.50,
#     "store_id": 1,
#     "store": {
#         "id": 1,
#         "name": "store name"
#     }
# }
#
# In the case of this other code:
#
# class StoreSchema(PlainStoreSchema):
#     items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
#
# It is basically the same, except we add fields.List, which means that we are expecting a list of items in contrast to ItemSchema where we expect a single store.
#
# Here is an example output of a store dump:
#
# {
#     "id": 1,
#     "name": "store name",
#     "items": [
#         {"id": 1, "name": "item name", "price": 13.50},
#         {"id": 2, "name": "item2 name", "price": 20.50}
#     ]
# }
