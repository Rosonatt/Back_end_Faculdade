from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["loja_db"]
collection = db["produtos"]

def create_product(product_data: dict):
    return collection.insert_one(product_data)

def get_all_products():
    return list(collection.find())

def get_product_by_id(product_id: ObjectId):
    return collection.find_one({"_id": product_id})

def update_product(product_id: ObjectId, product_data: dict):
    return collection.update_one({"_id": product_id}, {"$set": product_data})

def delete_product(product_id: ObjectId):
    return collection.delete_one({"_id": product_id})