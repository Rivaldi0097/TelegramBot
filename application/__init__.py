from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = '234949dfb30ae1a4d5d88c2a7b00d628a998e435'
app.config["MONGO_URI"] = 'mongodb+srv://Rivaldi:MtXq2qblSanIYB0o@mern.v5mpvvr.mongodb.net/shopping_app?retryWrites=true&w=majority'

#set up mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes

