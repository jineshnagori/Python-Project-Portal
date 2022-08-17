import flask
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/ml")
def ml():
    return render_template("ml.html")

@app.route("/dl")
def dl():
    return render_template("dl.html")

if __name__ == "__main__":
    app.run(debug=True)