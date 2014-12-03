#!/usr/bin/env python3.4
"""Main demo app."""

from models import db, User
from flask import Flask, jsonify, request, session, redirect, url_for


app = Flask(__name__)
db.init_app(app)
app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'postgresql:///scavenge',
    'SECRET_KEY': "change me! (and load from config file)",
})


@app.route('/')
def index():
    return app.send_static_file("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return app.send_static_file("login.html")
    email = request.form.get('email')
    user = User.query.filter_by(email=email).scalar()
    if not user:
        return "failure", 404
    session['user_id'] = user.id
    return redirect(url_for('index'))


@app.route('/api')
def basic_api():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter_by(id=user_id).scalar()
        return jsonify({'username': user.username, 'email': user.email})
    return jsonify({})

if __name__ == '__main__':
    app.run(port=5000)
