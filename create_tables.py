#!/usr/bin/env python3.4
"""Create the database and ensure a row exists."""
from models import db, User


def create_tables():
    db.create_all()


def ensure_user():
    if User.query.count() == 0:
        jake = User('jake', 'jake@gmail.com')
        db.session.add(jake)
        db.session.commit()


if __name__ == '__main__':
    create_tables()
    ensure_user()
