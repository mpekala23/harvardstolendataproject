from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True, unique=True)
    category = db.Column(db.String)
    author = db.Column(db.String)
    author_desc = db.Column(db.String)
    date = db.Column(db.Date)
    image = db.Column(db.LargeBinary)
    caption = db.Column(db.String)
    text = db.Column(db.String)
    chart1 = db.Column(db.LargeBinary)
    chart1_caption = db.Column(db.String)
    chart2 = db.Column(db.LargeBinary)
    chart2_caption = db.Column(db.String)
