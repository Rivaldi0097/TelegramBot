from application import app
from application import db

@app.route("/")
def get_products():

    for product in db.products.find():
        print(product)
    
    return "Hellow World!"