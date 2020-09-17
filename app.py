from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/")

@app.route("/scrape")
def scrape():

    site_data = scrape_mars.scrape_pages()
    mongo.db.collection.update({}, site_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def home():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", vacation=mars_data)
