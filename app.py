import json
from flask import Flask, render_template

app = Flask(__name__)

##Routes for beer time
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/whats-hot')
def hot():
    return render_template("whats-hot.html", page_title="Whats Hot")

@app.route('/our-favourites')
def favourites():
    data = []
    with open("static/data/beers.json", "r") as response:
        data = json.load(response)
    return render_template("our-favourites.html", page_title="Our Favourites", beers_list=data)

@app.route('/sign-in')
def signIn():
    return render_template("sign-in.html", page_title="Sign In")

@app.route('/contact')
def contact():
    return render_template("contact-us.html", page_title="Contact Us")