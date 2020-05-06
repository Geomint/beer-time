import os
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

# Create an instance of flask and assign it to 'app'.
app = Flask(__name__)

# Initilize connection to MongoDB.
app.config["MONGO_DBNAME"] = 'Beer-Time'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)

# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("pages/404.html"), 404

# Home page
@app.route('/')
def index():
    """
    This function is for the home page, it renders the index template and is the standard landing page for the site.
    """
    try:
        users = mongo.db.users
        return render_template("pages/index.html", body_id="home-page", page_title="Home", current_user=users.find_one({'name': session['username']}))
    except:
        return render_template("pages/index.html", body_id="home-page", page_title="Home")


# All beers page
@app.route('/all-beers')
def all_beers():
    """
    This function is for the all-beers page, this is the main focus of the website, the beers collection is accessed and made available to the HTML template.
    The favourites array of the current user in session is accessed and then passed into the favourites_beers_id array, which is then used to show the user which
    beer they currently have saved as a favourite.
    """
    try:
        users = mongo.db.users
        current_user_obj = users.find_one(
            {'name': session['username'].lower()})
        if len(current_user_obj['favourites']) != 0:
            current_user_favourites = current_user_obj['favourites']
        favourite_beers_id = []

        if len(current_user_obj['favourites']) != 0:
            for fav in current_user_favourites:
                current_beer = mongo.db.beers.find_one({'_id': fav})
                current_beer_id = current_beer['_id']
                favourite_beers_id.append(current_beer_id)

        return render_template("pages/beers/all-beers.html", favourite_beers_id=favourite_beers_id, beers=mongo.db.beers.find(), body_id="all-beers", current_user=users.find_one({'name': session['username'].lower()}))
    except:
        return redirect(url_for('create_account'))

# My list page
@app.route('/my-list', methods=["GET", "POST"])
def my_list():
    """
    This is the function for the my-list page, here the favourited beers are accessed through the current users object. The id's in the array are
    looped over in order to render them to the HTML.
    """
    users = mongo.db.users
    current_user_obj = users.find_one({'name': session['username'].lower()})
    current_user_favourites = current_user_obj['favourites']
    favourite_beers = []
    favourite_beers_id = []

    if len(current_user_obj['favourites']) != 0:
        for fav in current_user_favourites:
            current_beer = mongo.db.beers.find_one({'_id': fav})
            current_beer_id = current_beer['_id']
            favourite_beers_id.append(current_beer_id)

    for fav in current_user_favourites:
        current_beer = mongo.db.beers.find_one({'_id': fav})
        favourite_beers.append(current_beer)

    return render_template("pages/my-list.html", body_id="my-list", page_title="My List", favourite_beers_id=favourite_beers_id, favourite_beers=favourite_beers, current_user=users.find_one({'name': session['username'].lower()}))

# Add to favourites route
@app.route('/add-to-fav/<beer_id>', methods=['POST'])
def add_to_favourites(beer_id):
    """
    This is the function to handle adding or pushing beers into the current users favourites array. The current user object is selected from the session name and the beer_id
    is aquired through the url, this then gets pushed through into the favourites array.
    """
    users = mongo.db.users
    current_user_obj = users.find_one({'name': session['username'].lower()})
    mongo.db.users.update(
        current_user_obj, {"$push": {"favourites": ObjectId(beer_id)}})
    return redirect(url_for('my_list'))

# Remove from favourites route
@app.route('/remove-from-favourites/<beer_id>', methods=['POST'])
def remove_from_favourites(beer_id):
    """
    This is the function to handle removing or pulling beers out of the current users favourites array. The current user object is selected from the session name and the beer_id
    is aquired through the url, this then gets pulled or removed from the favourites array.
    """
    users = mongo.db.users
    current_user_obj = users.find_one({'name': session['username'].lower()})
    mongo.db.users.update(
        current_user_obj, {"$pull": {"favourites": ObjectId(beer_id)}})
    return redirect(url_for('my_list'))

# Beer page
@app.route('/beer/<beer_id>')
def beer_page(beer_id):
    """
    This is the function that creates the beer 'product-page' where the user can read more about the beer and view alternatives.
    """
    users = mongo.db.users
    the_beer = mongo.db.beers.find_one({"_id": ObjectId(beer_id)})
    you_might_like = mongo.db.beers.find().limit(3)
    test = mongo.db.reviews.find({'beer_id': ObjectId(beer_id)})
    reviews = []
    cur = test
    for i in cur:
        reviews.append(i)
    return render_template('pages/beers/beer.html', beer=the_beer, beer_reviews=reviews, you_might_like=you_might_like, body_id="beer-product", current_user=users.find_one({'name': session['username']}))

# Add Review route
@app.route('/add-review/<beer_id>', methods=["POST", "GET"])
def add_review(beer_id):
    """
    This function inserts user inputted reviews in to the reviews collection by taking the information from the request form and inserting into the collection.
    """
    mongo.db.reviews.insert({
        'name': request.form.get('name'),
        'review': request.form.get('review'),
        'beer_id': ObjectId(beer_id),
    })
    return redirect(url_for('beer_page', beer_id=beer_id))

# Delete Review route
@app.route('/delete-review/<review_id>', methods=["POST", "GET"])
def delete_review(review_id):
    """
    This function removes the selected review based on the id that is passed via the URL.
    """
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('all_beers'))

# Edit Review page
@app.route('/edit-review/<review_id>', methods=["POST", "GET"])
def edit_review(review_id):
    """
    This function constructs a version of the edit-review page with the review passed from the URL, the user can then edit the message and submit.
    """
    users = mongo.db.users
    review = mongo.db.reviews.find({"_id": ObjectId(review_id)})
    return render_template("pages/edit-review.html", body_id="edit-review-page", review=review, review_id=review_id, current_user=users.find_one({'name': session['username']}))

# Update Review route
@app.route('/update-review/<review_id>', methods=["POST", "GET"])
def update_review(review_id):
    """
    This function handles the updating of existing reviews within the collection, the review will only be updated against the message, not the id or name fields.
    """
    mongo.db.reviews.update({'_id': ObjectId(review_id)}, {
        '$set': {'review': request.form.get('review')}})
    return redirect(url_for('edit_review', review_id=review_id))

# Add beer page
@app.route('/add-beer')
def add_beer():
    """
    This is the function that creates the beer 'product-page' where the user can read more about the beer and view alternatives.
    """
    users = mongo.db.users
    return render_template('pages/beers/add-beer.html', body_id="add-beer", types=mongo.db.types.find(), current_user=users.find_one({'name': session['username'].lower()}))

# Insert beer route
@app.route('/insert-beer', methods=['POST'])
def insert_beer():
    """
    This is the function that gets triggered from the 'add-beer' page and handles the inserting of new documents into the database.
    The beer dictionary is constructed using the information collected from the HTML form.
    """
    beers = mongo.db.beers
    beers.insert_one(request.form.to_dict())
    return redirect(url_for('all_beers'))

# Edit beer page
@app.route('/edit-beer/<beer_id>')
def edit_beer(beer_id):
    """
    This is the function that handles the page in which the user can edit the beers, this function is only callable by the user with the admin setting.

    """
    users = mongo.db.users
    the_beer = mongo.db.beers.find_one({"_id": ObjectId(beer_id)})
    all_types = mongo.db.types.find()
    return render_template('pages/beers/edit-beer.html', body_id='edit-page', beer=the_beer, types=all_types, current_user=users.find_one({'name': session['username']}))

# Update beer route
@app.route('/update-beer/<beer_id>', methods=['POST'])
def update_beer(beer_id):
    """
    This function updates the beers in the database based on the beer_id from the url, this will update any value that is changed on the HTML form.
    """
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
    })
    return redirect(url_for('add_beer'))

# Delete beer route
@app.route('/delete-beer/<beer_id>')
def delete_beer(beer_id):
    """
    This function deletes the selected beer from the database based on the beer_id passed in from the url.
    """
    mongo.db.beers.remove({'_id': ObjectId(beer_id)})
    return redirect(url_for('all_beers'))

# Register Account page
@app.route('/register', methods=["GET", "POST"])
def create_account():
    """
    This is the function which handles the creation of new accounts on the website, if the request method is POST the code checks to see if the entered
    username exists in the database, it also checks to see if the passwords entered match for further validation. If the username doesnt exist and the passwords match
    the password is then encrypted using bcrypt and inserted into the users table in the database.
    """
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        favourites_array = []
        password = request.form['password']
        repeat_password = request.form['repeat_password']

        if password == repeat_password:
            if existing_user is None:
                hashpass = bcrypt.hashpw(
                    request.form['password'].encode('utf-8'), bcrypt.gensalt())
                users.insert({
                    'name': request.form['username'].lower(),
                    'password': hashpass,
                    'favourites': favourites_array
                })
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            flash('That username already exists, try something else.')
        flash('The passwords dont match.')
    return render_template("pages/account-nav.html", body_id="register-page", page_title="Create an Account")

# Sign-in page
@app.route('/sign-in', methods=["POST", "GET"])
def sign_in():
    """
    This is the function that renders the sign in page where users on the website can sign into their accounts.
    """
    return render_template("pages/account-nav.html", body_id="sign-in", page_title="Sign In")

# log-in route
@app.route('/login', methods=["POST", "GET"])
def login():
    """
    This is the function that checks if the user exists in the database, and populates that value inside the login_user variable.
    """
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username'].lower()})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    flash('That username/password combination was incorrect')
    return redirect(url_for('sign_in'))

# sign-out route
@app.route('/sign-out')
def sign_out():
    """
    This function clears the session when the route is accessed.
    """
    session.clear()
    return redirect('/')

# Contact Page
@app.route('/contact', methods=["GET", "POST"])
def contact():
    """
    This is the contact page for beertime, users can input messages into the relevant fields and send a message to the database, a flashed response message notifies the user that some action has been taken.
    """
    try:
        users = mongo.db.users
        if request.method == "POST":
            flash("Thanks {} we have recieved your message! A member of our team will be in touch shortly".format(
                request.form["name"]))
        return render_template("pages/contact-us.html", body_id="contact-page", page_title="Contact Us", current_user=users.find_one({'name': session['username']}))
    except:
        if request.method == "POST":
            flash("Thanks {} we have recieved your message! A member of our team will be in touch shortly".format(
                request.form["name"]))
        return render_template("pages/contact-us.html", body_id="contact-page", page_title="Contact Us")


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
