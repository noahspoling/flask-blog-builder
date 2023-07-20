from flask import Blueprint, jsonify, request, render_template


# from markdown_cms.posts.services import create_post, get_all_posts, get_post_by_id, update_post, delete_post


routesBlueprint = Blueprint('main', __name__)

@routesBlueprint.route('/')
def index():
    return render_template("index.html")
    
@routesBlueprint.route('/Posts')
def posts():
    return render_template("posts.html")

@routesBlueprint.route('/Projects')
def projects():
    return render_template("projects.html")
  
@routesBlueprint.route('/AboutMe')
def aboutMe():
    return render_template("about.html")

@routesBlueprint.route('/ContactMe')
def contactMe():
    return render_template("contact.html")
