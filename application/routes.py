from application import app
from flask import flash, redirect, render_template, request
import json
from application.models import User
from application.forms import LoginForm, RegisterForm


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

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        #if form.email.data == "gospelin.gi@gmail.com":
        if request.form.get("email") == "gospelin.gi@gmail.com":
            flash("You have been logged in!", "success-msg")
            return redirect("/index")
        else:
            flash("Login Unsuccessful. Please check email and password", "error-msg")
    return render_template("login.html", title="Login", form=form, login=True)
