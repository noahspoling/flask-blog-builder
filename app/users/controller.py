from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.users.form import LoginForm, RegistrationForm
from app.users.model import User
from flask_login import LoginManager

login = LoginManager()

@login.user_loader
def load_user(id):
    return User.Query.get(int(id))

userBlueprint = Blueprint('posts', __name__, url_prefix="/user")

@userBlueprint('/login', methods=["GET", "POST"])
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

