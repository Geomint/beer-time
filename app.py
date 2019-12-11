from flask import Flask, render_template

app = Flask(__name__)

##Routes for beer time
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact-us.html")