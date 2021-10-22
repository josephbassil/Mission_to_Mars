from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app=Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config['MONGO_URI']='mongodb://localhost:27017/mars_app'
mongo=PyMongo(app)

#let's define the flask route for our html page
@app.route("/")
def index():
    mars=mongo.db.mars.find_one()
    return render_template('index.html',mars=mars)

#This function is what links our code to our web app

#Now let's add the next route and function to our code:
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()