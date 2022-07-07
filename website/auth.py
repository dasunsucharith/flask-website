from flask import Blueprint, render_template, request, flash
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('name must be greater than 1 characters.', category='error')
        elif password != password_confirm:
            flash('Password do not match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            #add user to database
            new_user = User(name=name, email=email, password=password) 
            flash('Account Created!', category='success')
    return render_template("sign_up.html")