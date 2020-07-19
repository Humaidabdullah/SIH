from flask import Flask
from flask_pymongo import pymongo
from app import app
CONNECTION_STRING = "mongodb+srv://humaid:humaid@cluster0-toj2u.azure.mongodb.net/appdata?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('appdata')
# user_collection = pymongo.collection.Collection(db, 'user')