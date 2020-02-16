import os
from flask import Flask, render_template, request, flash, session, redirect, url_for
import json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Beer-Time'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = "vRb81oq80xFpG45So4CKACqU1GvA9Fv"

mongo = PyMongo(app)

# Routes for beer time


@app.route('/delete-beer/<beer_id>')
def delete_beer(beer_id):
    mongo.db.beers.remove({'_id': ObjectId(beer_id)})
    return redirect(url_for('all_beers'))


@app.route('/edit-beer/<beer_id>')
def edit_beer(beer_id):
    the_beer = mongo.db.beers.find_one({"_id": ObjectId(beer_id)})
    all_types = mongo.db.types.find()
    return render_template('beers/edit-beer.html', beer=the_beer, types=all_types)


@app.route('/update_beer/<beer_id>', methods=['POST'])
def update_beer(beer_id):
    beer = mongo.db.beers
    beer.update({'_id': ObjectId(beer_id)},
                {
                'name': request.form.get('name'),
                'brewery': request.form.get('brewery'),
                'type': request.form.get('type'),
                'excerpt': request.form.get('excerpt'),
                'notes': request.form.get('notes'),
                'abv': request.form.get('abv'),
                'image': request.form.get('image')
                }
                )
    return redirect(url_for('add_beer'))


@app.route('/all-beers')
def all_beers():
    return render_template("beers/all-beers.html", beers=mongo.db.beers.find(), body_id="all-beers")


@app.route('/add-beer')
def add_beer():
    return render_template('beers/add-beer.html', body_id="add-beer", types=mongo.db.types.find())


@app.route('/insert-beer', methods=['POST'])
def insert_beer():
    beers = mongo.db.beers
    beers.insert_one(request.form.to_dict())
    return redirect(url_for('all_beers'))


"""
Route for the home page
"""
@app.route('/')
def index():
    data = []
    with open("static/data/beers.json", "r") as response:
        data = json.load(response)
    return render_template("index.html", body_id="home-page", page_title="Home", beers_list=data)


"""
Route for the 'whats-hot' page
"""
@app.route('/whats-hot')
def hot():
    with open("static/data/popular-beers.json", "r") as response:
        data = json.load(response)
    return render_template("whats-hot.html", body_id="whats-hot", page_title="What's Hot", beers_list=data)


"""
Route for the 'our-favourites' page
"""
@app.route('/our-favourites')
def favourites():
    data = []
    with open("static/data/beers.json", "r") as response:
        data = json.load(response)
    return render_template("our-favourites.html", body_id="our-favourites", page_title="Our Favourites", beers_list=data)


"""
Route for the our favourites, individual beer page, the url takes the beer_name and appends it on the url after /our-favourites/
opening the beers.json file to read and storing that data in 'response' to check that the url is equal to beer_name. If true
return the beer.html page where the user will see the selected beer.
"""
@app.route('/our-favourites/<beer_name>')
def about_beer(beer_name):
    beer = {}

    with open("static/data/beers.json", "r") as response:
        data = json.load(response)
        for obj in data:
            if obj["url"] == beer_name:
                beer = obj

    return render_template("beers/beer.html", beer=beer)


@app.route('/my-list', methods=["GET", "POST"])
def myList():
    return render_template("my-list.html", body_id="my-list", page_title="My List")


"""
Route for the sign-in page
"""
@app.route('/sign-in', methods=["GET", "POST"])
def signIn():

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect('/my-list')

    return render_template("sign-in.html", body_id="sign-in", page_title="Sign In")


@app.route('/beer-page')
def beerPage():
    return render_template("beer-page.html", body_id="beer-page", page_title="beer-page")


"""
Route for sign-out
"""
@app.route('/sign-out')
def signOut():
    session.clear()
    return redirect('/')


"""
Route for the contact page
"""
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {} we have recieved your message!".format(
            request.form["name"]))
    return render_template("contact-us.html", body_id="contact-page", page_title="Contact Us")


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
