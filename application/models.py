import flask
from application import db


class User(db.Document):
    user_id = db.IntField(unique=False, null=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    gender = db.StringField(max_length=10)
    date_of_birth = db.StringField(max_length=10)
    state = db.StringField(max_length=15)
    local_government_area = db.StringField(max_length=20)
    course_of_study = db.StringField(max_length=20)
    phone_number = db.StringField(max_length=15)
