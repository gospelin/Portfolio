from application import app
from flask import render_template
import json


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=True)


@app.route("/sample")
def sample():
    return render_template("sample.html", login=True)


@app.route("/more")
def more():
    return render_template("more.html", login=True)


@app.route("/contact")
def contact():
    return render_template("contact.html", login=True)


@app.route("/register")
def register():
    return render_template("register.html", login=True)


@app.route("/enroll")
def enroll():
    with open("./application/templates/data/nigerian_data.json", 'r') as data:
        enrollData = json.load(data)

    return render_template("enroll.html", login=True, enrollData=enrollData )


@app.route("/login")
def login():
    return render_template("login.html", login=False)


if __name__ == "__main__":
    app.run(debug=True)
