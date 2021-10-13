import os
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

app = flask.Flask(
    __name__, template_folder="./web/templates", static_folder="./web/static"
)
app.config.update(
    DEBUG=True,
    SECRET_KEY=os.getenv("SECRET_KEY"),
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL"),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    TEMPLATES_AUTO_RELOAD=True,
)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(4094))
    artists = db.Column(db.PickleType)


db.create_all()


class Person:
    def __init__(self):
        self.id = None
        self.artists = self.get_artists() or []
        self.logged_in = False

    def get_artists(self):
        if self.id:
            return User.query.filter_by(id=self.id).one().artists
        else:
            return []


person = Person()

# callback to reload the user object
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
