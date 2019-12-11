from flask import Flask, render_template

app = Flask(__name__)

##Routes for beer time
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/whats-hot')
def hot():
    return render_template("whats-hot.html")

@app.route('/our-favourites')
def favourites():
    return render_template("our-favourites.html")

@app.route('/sign-in')
def signIn():
    return render_template("sign-in.html")

@app.route('/contact')
def contact():
    return render_template("contact-us.html")