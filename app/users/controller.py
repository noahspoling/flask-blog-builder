from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.users.form import LoginForm, RegistrationForm
from app.users.model import User
from app import db


userBlueprint = Blueprint('users', __name__, url_prefix="/user")

@userBlueprint.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.valiate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@userBlueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@userBlueprint.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash('User registered')
            return redirect(url_for('login'))
        except Exception as e:
            print(f"An error occurred: {e}")
        
        return render_template('register.html', title='Register', form=form)
    
@userBlueprint.route('/index')
@login_required
def index():
    return "Hello, " + current_user.username

@userBlueprint.route('/isLoggedIn', methods=["GET"])
def checkSignedIn():
    if current_user:
        return ''.join(render_template('htmx/navbarSignedIn.html'))
    else:
        return ''.join(render_template('htmx/navbarSignedOut.html'))