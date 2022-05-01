from flask_app import app
from flask import jsonify
from flask import render_template, redirect, session
from flask_app.models import models_user

@app.route('/')
def index():
    if 'loginid' in session:
        user=models_user.User.select_one({'id': session['loginid']})
    else:
        user = {
            'full_name': 'guest'
        }
    return render_template('index.html', user=user)


@app.route('/signin')
def login_register():
    if 'loginid' in session:
        user=models_user.User.select_one({'id': session['loginid']})
    else:
        user = {
            'full_name': 'guest'
        }
    return render_template('login_registration.html', user=user)

@app.route('/dashboard')
def dashboard():
    if 'loginid' in session:
        user=models_user.User.select_one({'id': session['loginid']})
    else:
        user = {
            'full_name': 'guest'
        }
    return render_template('dashboard.html', user=user)

@app.route('/browse')
def browse():
    if 'loginid' in session:
        user=models_user.User.select_one({'id': session['loginid']})
    else:
        user = {
            'full_name': 'guest'
        }
    return render_template('browse_sets.html', user=user)