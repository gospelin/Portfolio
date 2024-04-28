from application import app
from flask import render_template


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


@app.route("/login")
def login():
    return render_template("login.html", login=False)


if __name__ == "__main__":
    app.run(debug=True)
