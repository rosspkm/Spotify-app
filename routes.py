import os
from __init__ import app, person, User
import flask
from utils.functions import (
    add_to_db,
    validate_password,
    validate_username,
    submit_artist,
)
import utils.encrypt.encryption as encryption

from flask_login import login_required, login_user, logout_user, current_user
from src.main import call_apis, get_new, music_search, check_artist


@app.route("/")
def index():
    return flask.render_template(
        "index.html", data=get_new(), logged_in=person.logged_in
    )


@app.route("/discovery")
@login_required
def discovery():
    is_empty = False if len(person.artists) else True

    return flask.render_template(
        "discovery.html", lst=call_apis(artists=person.artists), is_empty=is_empty
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return flask.redirect("/")

    if flask.request.method == "POST":
        user = User.query.filter_by(username=flask.request.form["username"]).first()
        password = encryption.Encryption(flask.request.form["password"]).encrypt()

        if user and user.password == password:
            person.id = user.id
            person.logged_in = True
            login_user(user)
            return flask.redirect("/")

        elif not user or not password:
            flask.flash("Invalid username or password")

        else:
            return flask.abort(401)
    else:
        return flask.render_template("login.html")

    return flask.redirect("/login")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return flask.redirect("/")

    if flask.request.method == "POST":
        username = flask.request.form["username"]
        password = flask.request.form["password"]
        if (
            validate_password(password)
            and not User.query.filter_by(username=username).first()
            and validate_username(username)
        ):
            password = encryption.Encryption(password).encrypt()
            user = User(
                username=username,
                password=password,
            )
            add_to_db(user)
            user = User.query.filter_by(username=username).first()
            person.id = user.id
            person.logged_in = True
            login_user(user)
            return flask.redirect("/")

        elif User.query.filter_by(username=username).first():
            flask.flash("Username already exists")

        elif not validate_password(password):
            flask.flash(
                "Must be at least 8 characters and contain at least 1 uppercase letter, 1 lowercase letter, 1 number and 1 special character"
            )
        elif not validate_username(username):
            flask.flash("Username can not be that, only alphanumeric characters")

    else:
        return flask.render_template("signup.html")

    return flask.redirect("/signup")


@app.route("/lookup", methods=["POST"])
def lookup():
    if flask.request.method == "POST":
        search = flask.request.form["search"]
        param = flask.request.form["type"]
        if search and param:
            return flask.redirect(f"/search?type={param}&search={search}")

        return flask.abort(404)


@app.route("/search")
def search():
    search_type = flask.request.args.get("type")
    search = flask.request.args.get("search")

    music = music_search(search_type, search)
    is_empty = False if len(music) else True

    return flask.render_template(
        "search.html", search_type=search_type, music_search=music, is_empty=is_empty
    )


@app.route("/addArtist", methods=["POST"])
def addartist():
    if flask.request.method == "POST":
        value = flask.request.form["add"]
        task = flask.request.form["task"]
        if not check_artist(value) and task == "insert":
            flask.flash("Please enter a valid artist ID")

        else:
            if task == "remove":

                try:
                    person.artists.remove(value)
                    User.query.filter_by(id=person.id).update(
                        {"artists": person.artists}
                    )
                    submit_artist()
                    flask.flash("Removed artist from discovery")
                except:
                    flask.flash("No artist with that ID exists in your discovery")

            elif task == "insert":

                if value in person.artists:
                    flask.flash("Artist is already in your discovery")
                else:
                    person.artists.append(value)
                    flask.flash("Successfully added artist to your discovery")

                User.query.filter_by(id=person.id).update({"artists": person.artists})
                submit_artist()
        return flask.redirect(flask.url_for("discovery"))


@app.route("/logout")
@login_required
def logout():
    person.logged_in = False
    logout_user()
    return flask.redirect("/")


app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 4141)), debug=True)
