from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user, login_required
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
import app

def custom_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('You need to be an author to access this page.')
            return redirect(url_for('main.loginRequired')) 
        return f(*args, **kwargs)
    return decorated_function

def author_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('You need to be an author to access this page.')
            return redirect(url_for('main.loginRequired')) 
        elif not current_user.isAuthor:
            flash('You need to be an author to access this page.')
            return redirect(url_for('main.AuthorRequired')) 
        return f(*args, **kwargs)
    return decorated_function

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

def send_email(to, subject, template):
    message = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )