from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import os
# From the separate python file in this directory, we'll import the code that is used to scrape mars
import scrape_mars

app = Flask(__name__)
# Use flask_pymongo to set up mongo connection

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# This route will query the Mongo database and get the mars result
# and then render them to the html file

@app.route("/")
def index():
    
    mars= mongo.db.collection.find_one()
    #mongo.db.collection.find_one()
    return render_template("index.html", mars=mars)

# This route will trigger the webscraping, but it will then send us 
# back to the index route to render the results

@app.route("/scrape")
def scrape():
# drop any data that is already in database
    #db.mars.drop()
    
    mars = scrape_mars.scrape()
    mongo.db.collection.update({}, mars, upsert=True)
    return "Scraping Successful"
    
    # Use Flask's redirect function to send us to a different route once this task has completed.
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)