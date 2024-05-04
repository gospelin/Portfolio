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
    user_id = db.IntField(unique=False, null=True)
    first_name = db.StringField( max_length = 50 )
    last_name = db.StringField( max_length = 50 )
    gender = db.StringField( max_length = 10 )
    date_of_birth = db.StringField(max_length=10)
    state = db.StringField(max_length=15)
    local_government_area = db.StringField(max_length=20)
    course_of_study = db.StringField(max_length=20)
    phone_number = db.StringField(max_length=15)

@app.route("/user")
def user():
    User(
        first_name="Brianna",
        last_name="Howard",
        gender="Female",
        date_of_birth="1977-09-29",
        state="Zamfara",
        local_government_area="Bungudu",
        course_of_study="Law",
        phone_number="+2347222406665",
    ).save()
    users = User.objects.all()
    return render_template("user.html", login=True, users=users)

@app.route("/login")
def login():
    return render_template("login.html", login=False)
