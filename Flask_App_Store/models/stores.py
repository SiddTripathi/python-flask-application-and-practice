from ..db import db


#This will act as a mapping between a database row and python class as well as object (json)
class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store",lazy="dynamic", cascade="all, delete, delete-orphan")
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")
     #cascade makes sure that in SQL Lite or alchemy if the store is deleted the items are also deleted as we know that SQLAlchemy and sql lite the concept of foreign key
     #does not work