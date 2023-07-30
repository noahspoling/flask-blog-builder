from functools import wraps
from flask import redirect, url_for
from flask_login import current_user, login_required

def author_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.isAuthor:
            return redirect(url_for('main_route'))  # Replace with your own route
        return f(*args, **kwargs)
    return decorated_function
