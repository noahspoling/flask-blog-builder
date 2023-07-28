from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify
from app.posts.forms import PostForm
from app.posts.service import createPost, getAllPosts, getPostById, updatePost, deletePost

postsBlueprint = Blueprint('posts', __name__, url_prefix="/api/v1")

@postsBlueprint.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@postsBlueprint.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        post = createPost(title=form.title.data, content=form.content.data)
        return redirect(url_for('posts.post_detail', post_id=post.id))
    return jsonify({"error": "Validation failed", "errors": form.errors}), 400

@postsBlueprint.route('/post', methods=['GET'])
def posts_list():
    try:
        posts = getAllPosts()
        if posts is None:
            return jsonify({"error": "could not fetch posts"}), 400
        return render_template('posts_list.html', posts=posts)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e #Will return error page
    

@postsBlueprint.route('/post/<int:post_id>')
def post_detail(post_id):
    try:
        post = getPostById(post_id)
        return render_template('post_detail.html', post=post)
    except:
        return #Will return error page

@postsBlueprint.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    try:
        deletePost(post_id)
        return redirect(url_for('posts_list'))  # Redirect to the list of posts after deletion
    except:
        return #Will return error page
    