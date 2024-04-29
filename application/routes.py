from application import app, db
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

class User(db.Document):
    user_id = db.StringField( unique = True )
    first_name = db.StringField( max_length = 50 )
    last_name = db.StringField( max_length = 50 )
    email = db.StringField( max_length = 30 )
    password = db.StringField( max_length = 30 )

@app.route("/user")
def user():
    #User(user_id = "1", first_name = "John", last_name = "Doe", email = "johndoe@example.com", password = "password").save()
    #User(user_id = "2", first_name = "Jane", last_name = "Doe", email = "janedoe@example.com", password = "admin123").save()
    users = User.objects.all()
    return render_template("user.html", login=True, users=users)

@app.route("/login")
def login():
    return render_template("login.html", login=False)

