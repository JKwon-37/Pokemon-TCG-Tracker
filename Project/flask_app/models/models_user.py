from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app import DATABASE, bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['pw']
        self.confirm_password = data['confirm_pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def select_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('livestream_shop').query_db(query)
        if results:
            users = []
            for u in results:
                users.append( cls(u) )
            return users
        return False

    @classmethod
    def select_one(cls,data:dict):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('livestream_shop').query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def select_one_by_email(cls,data:dict):
        query  = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('livestream_shop').query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, pw, confirm_pw) VALUES (%(first_name)s,%(last_name)s,%(email)s, %(pw)s, %(confirm_pw)s);"
        # comes back as the new row id
        result = connectToMySQL('livestream_shop').query_db(query,data)
        return result

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s, pw=%(pw)s, confirm_pw=%(confirm_pw)s WHERE id = %(id)s;"
        return connectToMySQL('livestream_shop').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('livestream_shop').query_db(query,data)

    @staticmethod
    def login_validator(form_data:dict):
        is_valid = True

        if len(form_data['email']) <= 0:
            flash("Email is required!", "err_users_email_login")
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!", "err_users_email_login")
            is_valid = False

        if len(form_data['pw']) <= 0:
            flash("Password is required!", "err_users_pw_login")
            is_valid = False

        if is_valid:
            potential_user = User.select_one_by_email({'email': form_data['email']})
            print(potential_user)
            if potential_user:
                if not bcrypt.check_password_hash(potential_user.password, form_data['pw']):
                    is_valid = False
                    flash("Invalid credentials!", "err_users_pw_login")
                else:
                    session['loginid'] = potential_user.id
            else:
                is_valid = False
                flash("Invalid credentials!", "err_users_pw_login")

        return is_valid

    @staticmethod
    def registration_validator(form_data:dict):
        is_valid = True

        if len(form_data['first_name']) <= 0:
            flash("First name is required!", "err_users_first_name")
            is_valid = False
        elif len(form_data['first_name']) < 2:
            flash("First name must be at least 2 characters!", "err_users_first_name")
            is_valid = False

        if len(form_data['last_name']) <= 0:
            flash("Last name is required!", "err_users_last_name")
            is_valid = False
        elif len(form_data['last_name']) < 2:
            flash("Last name must be at least 2 characters!", "err_users_last_name")
            is_valid = False

        if len(form_data['email']) <= 0:
            flash("Email is required!", "err_users_email")
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!", "err_users_email")
            is_valid = False
        else:
            potential_user = User.select_one_by_email({'email':form_data['email']})
            if potential_user:
                flash("Email already exists!", "err_users_email")
                is_valid = False

        if len(form_data['pw']) <= 0:
            flash("Password is required!", "err_users_pw")
            is_valid = False
        elif len(form_data['pw']) < 8:
            flash("Password must be at least 8 values!", "err_users_pw")
            is_valid = False

        if len(form_data['confirm_pw']) <= 0:
            flash("Confirm password is required!", "err_users_confirm_pw")
            is_valid = False
        elif len(form_data['confirm_pw']) < 8:
            flash("Password must be at least 8 values!", "err_users_confirm_pw")
            is_valid = False
        elif form_data['pw'] != form_data['confirm_pw']:
            is_valid = False
            flash("Passwords do not match.", "err_users_confirm_pw")

        return is_valid
