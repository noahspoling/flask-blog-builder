from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify
from app.posts.forms import PostForm
from app.posts.service import createPost, getAllPosts, getPostById, updatePost, deletePost

postsBlueprint = Blueprint('posts', __name__, url_prefix="/api/v1")

@postsBlueprint.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@postsBlueprint.route('/post', methods=['POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        post = createPost(title=form.title.data, content=form.content.data)
        return jsonify(post.toDictionary()), 201 
    return jsonify({"error": "Validation failed", "errors": form.errors}), 400

@postsBlueprint.route('/render/post', methods=['GET'])
def posts_list():
    try:
        posts = getAllPosts()
        if posts is None:
            return jsonify({"error": "could not fetch posts"}), 400
        return ''.join(render_template('htmx/post.html', post=post) for post in posts)
        #return jsonify([post.toDictionary() for post in posts]), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred"}), 500
    
#This returns an object rather than html files for third party apps that might handle data differently
@postsBlueprint.route('/post', methods=['GET'])
def posts_list_object():
    try:
        posts = getAllPosts()
        if posts is None:
            return jsonify({"error": "could not fetch posts"}), 400
        return jsonify([post.toDictionary() for post in posts]), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred"}), 500

@postsBlueprint.route('/post/<int:post_id>', methods=["PUT"])
def post_update(post_id):
    return
@postsBlueprint.route('/render/post/<int:post_id>', methods=['GET'])
def post_detail(post_id):
    try:
        post = getPostById(post_id)
        post = updatePost(postId=post_id, title=post.title, content=post.content)
        return render_template('post_detail.html')
        #return jsonify(post.toDictionary()), 200
    except:
        return jsonify({"error": "An error occurred"}), 500
    
@postsBlueprint.route('/post/<int:post_id>', methods=['GET'])
def post_detail_object(post_id):
    try:
        post = getPostById(post_id)
        post = updatePost(postId=post_id, title=post.title, content=post.content)
        return jsonify(post.toDictionary()), 200
    except:
        return jsonify({"error": "An error occurred"}), 500

@postsBlueprint.route('/post/<int:post_id>/delete', methods=['DELETE'])
def delete_post(post_id):
    try:
        deletePost(post_id)
        return jsonify({"message": "Post deleted"}), 200  # Redirect to the list of posts after deletion
    except:
        return jsonify({"error": "An error occurred"}), 500

    