from flask import Blueprint, jsonify, request


# from markdown_cms.posts.services import create_post, get_all_posts, get_post_by_id, update_post, delete_post


app = Blueprint('main', __name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/Posts')
def posts():
    return render_template("posts.html")

@app.route('/Projects')
def projects():
    return render_template("projects.html")
  
@app.route('/AboutMe')
def aboutMe():
    return render_template("about.html")

@app.route('/ContactMe')
def contactMe():
    return render_template("contact.html")
