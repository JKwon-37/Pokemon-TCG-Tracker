from flask_app import app, bcrypt
from flask import request, redirect, session, render_template
from flask_app.models import models_user


@app.route('/register', methods=['POST'])
def register():
    if not models_user.User.registration_validator(request.form):
        return redirect('/signin')

    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    confirm_pw_hash = bcrypt.generate_password_hash(request.form['confirm_pw'])
    data = {
        **request.form,
        'pw': pw_hash,
        'confirm_pw': confirm_pw_hash
    }
    id = models_user.User.add_user(data)
    session['loginid'] = id
    return redirect('/signin')

@app.route('/login', methods=['POST'])
def login():
    if not models_user.User.login_validator(request.form):
        return redirect('/signin')
    
    return redirect('/')

@app.route('/logout')
def logout():
    del session['loginid']
    return redirect('/signin')


