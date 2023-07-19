from app import db
from app.posts.model import Post
from markdown import markdown

def createPost(title, content):
    html_content = markdown(content)
    post = Post(title=title, content=content, html_content=html_content)
    db.session.add(post)

    # TODO: Add rollback support
    db.session.commit()
    return post

def getAllPosts():
    return Post.query.all()

def getPostById(postId):
    return Post.query.get_or_404(postId)

def updatePost(postId, title, content):
    post = getPostById(postId)
    post.title = title
    post.content = content
    post.html_content = markdown(content)
    db.session.commit()
    return post

def deletePost(postId):
    post = getPostById(postId)
    db.session.delete(post)
    db.session.commit()
