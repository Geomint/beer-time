import os
from flask import Flask, render_template, request, flash, session, redirect, url_for
import json
import bcrypt
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Beer-Time'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = "vRb81oq80xFpG45So4CKACqU1GvA9Fv"

mongo = PyMongo(app)

# Routes for beer time

"""
This app route is for the index page, this accesses the beers collection in order to output a list of beers 
onto the slider toward the bottom of the page. 
"""
@app.route('/')
def index():
    return render_template("index.html", body_id="home-page", page_title="Home")


@app.route('/beer/<beer_id>')
def beer_page(beer_id):
    the_beer = mongo.db.beers.find_one({"_id": ObjectId(beer_id)})
    return render_template('beers/beer.html', beer=the_beer)


@app.route('/add-to-fav/<beer_id>', methods=['POST'])
def addToFavourites(beer_id):
    current_user = session['username']
    users = mongo.db.users
    current_user_obj = users.find_one({'name': session['username']})
    current_user_favourites = current_user_obj['favourites']
    mongo.db.users.update(
        current_user_obj, {"$push": {"favourites": ObjectId(beer_id)}})
    return redirect(url_for('myList'))


@app.route('/remove-from-favourites/<beer_id>', methods=['POST'])
def remove_from_favourites(beer_id):
    current_user = session['username']
    users = mongo.db.users
    current_user_obj = users.find_one({'name': session['username']})
    current_user_favourites = current_user_obj['favourites']
    mongo.db.users.update(
        current_user_obj, {"$pull": {"favourites": ObjectId(beer_id)}})
    return redirect(url_for('myList'))


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
    current_user = session['username']
    users = mongo.db.users
    current_user_obj = users.find_one({'name': session['username']})
    if len(current_user_obj['favourites']) != 0:
        current_user_favourites = current_user_obj['favourites']
    favourite_beers_id = []

    if len(current_user_obj['favourites']) != 0:
        for fav in current_user_favourites:
            current_beer = mongo.db.beers.find_one({'_id': fav})
            current_beer_id = current_beer['_id']
            favourite_beers_id.append(current_beer_id)

    return render_template("beers/all-beers.html", favourite_beers_id=favourite_beers_id, beers=mongo.db.beers.find(), body_id="all-beers", current_user=users.find_one({'name': session['username']}))


@app.route('/add-beer')
def add_beer():
    return render_template('beers/add-beer.html', body_id="add-beer", types=mongo.db.types.find())


@app.route('/insert-beer', methods=['POST'])
def insert_beer():
    beers = mongo.db.beers
    beers.insert_one(request.form.to_dict())
    return redirect(url_for('all_beers'))


@app.route('/my-list', methods=["GET", "POST"])
def myList():
    current_user = session['username']
    users = mongo.db.users
    current_user_obj = users.find_one({'name': session['username']})
    current_user_favourites = current_user_obj['favourites']
    favourite_beers = []

    for fav in current_user_favourites:
        current_beer = mongo.db.beers.find_one({'_id': fav})
        favourite_beers.append(current_beer)

    return render_template("my-list.html", body_id="my-list", page_title="My List", favourite_beers=favourite_beers, current_user=users.find_one({'name': session['username']}))


@app.route('/register', methods=["GET", "POST"])
def createAccount():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        favourites_array = []

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({
                'name': request.form['username'],
                'password': hashpass,
                'favourites': favourites_array
            })
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That Username Already Exists!'

    return render_template("create-account.html", body_id="register-page", page_title="Create an Account")


"""
Route for the sign-in page
"""
@app.route('/login', methods=["POST"])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return 'invalid user/pass'


@app.route('/sign-in', methods=["POST", "GET"])
def signIn():
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
