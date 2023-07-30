from flask_login import LoginManager

login = LoginManager()

@login.user_loader
def load_user(id):
    return User.Query.get(int(id))

userBlueprint = Blueprint('posts', __name__, url_prefix="/user")

@userBlueprint('/login', methods=[])
