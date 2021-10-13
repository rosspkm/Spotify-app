import re
from __init__ import db, person


def validate_password(password: str):
    return (
        True
        if re.match(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
            password,
        )
        else False
    )


def validate_username(username: str):
    return True if re.match(r"^[a-zA-Z0-9]+$", username) else False


def add_to_db(info):
    db.session.add(info)
    db.session.commit()


def submit_artist():
    db.session.commit()


def remove_from_db(info):
    db.session.delete(info)
    db.session.commit()
