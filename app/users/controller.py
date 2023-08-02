from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.users.form import LoginForm, RegistrationForm
from app.users.model import User
from app import db
#from app.users.authCheck import confirm_token

userBlueprint = Blueprint('users', __name__, url_prefix="/users")

@userBlueprint.route('/login', methods=["GET", "POST"])
def login():
    print("Login route accessed")
    if current_user.is_authenticated:
        print("User is already logged in")
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        if user is None or not user.check_password(form.password.data):
            print('Invalid username or password')
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        print("user logged in")
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@userBlueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@userBlueprint.route('/register', methods=["GET", "POST"])
def register():
    print("Register route accessed")
    if current_user.is_authenticated:
        print("User is already logged in")
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        print(user)
        try:
            db.session.add(user)
            db.session.commit()
            flash('User registered')
            print('User registered')
            print(user)
            return redirect(url_for('login'))
        except Exception as e:
            print(f"An error occurred: {e}")
    print("Returns to register")
    return render_template('register.html', title='Register', form=form)
    
@userBlueprint.route('/index')
@login_required
def index():
    return "Hello, " + current_user.username

@userBlueprint.route('/isLoggedIn', methods=["GET"])
def checkSignedIn():
    if current_user.is_authenticated:
        return ''.join(render_template('htmx/navbarSignedIn.html'))
    else:
        return ''.join(render_template('htmx/navbarSignedOut.html'))

#Renders template from query param based on if they are an author
@userBlueprint.route('/isAuthor', methods=["GET"])
def checkIfAuthor():
    template_name = request.args.get('template', 'htmx/addContentButton.html')
    if not current_user.isAuthor:
        return ''.join(render_template(template_name))
    else:
        return
    
@userBlueprint.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.emailVerified:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.emailVerified = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for("main.index"))
