from flask import Blueprint, jsonify, request, render_template


# from markdown_cms.posts.services import create_post, get_all_posts, get_post_by_id, update_post, delete_post


routesBlueprint = Blueprint('main', __name__)

# Navigation Bar routes

@routesBlueprint.route('/')
def index():
    return render_template("index.html")
    
@routesBlueprint.route('/Posts')
def posts():
    return render_template("posts.html")

@routesBlueprint.route('/AddContent')
def addContent():
    return render_template("addContent.html")

@routesBlueprint.route('/Projects')
def projects():
    return render_template("projects.html")
  
@routesBlueprint.route('/AboutMe')
def aboutMe():
    return render_template("about.html")

@routesBlueprint.route('/ContactMe')
def contactMe():
    return render_template("contact.html")

# Form Routes

# Login existing user

@routesBlueprint.route('/LoginForm')
def loginForm():
    return render_template("login.html")

# Form for a new user

@routesBlueprint.route('/RegisterForm')
def registerForm():
    return render_template("register.html")

# Route for form to submit the change password request to an email

@routesBlueprint.route('/ForgotPasswordForm')
def forgotPasswordForm():
    return render_template("forgotPassword.html")

# Route for the link sent in an email to change the password

@routesBlueprint.route('/ChangeForgottenPasswordForm')
def changeForgottenPasswordForm():
    return render_template("changeForgottenPassword.html")

# Change the password of a logged in user

@routesBlueprint.route('/ChangePasswordForm')
def changePasswordForm():
    return render_template("changePassword.html")
