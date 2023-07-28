from app import db
from app.posts.model import Post
from markdown import markdown
from bleach import clean
from datetime import date

allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 
                'em', 'i', 'li', 'ol', 'strong', 'ul']

def createPost(title, content):
    # takes content and turns it into html
    html_content = markdown(content)
    safe_html = clean(html_content, tags=allowed_tags)

    post = Post(title=title,
                content=content,
                html_content=safe_html,
                published_at=date.today(),
                updated_at=date.today()
                )
    try:
        db.session.add(post)
        db.session.commit()
        return post
    except:
        print("An error occurred")
        return

def getAllPosts():
    try:
        return Post.query.all()
    except:
        return
    

def getPostById(postId):
    try:
        return Post.query.get_or_404(postId)
    except:
        return
    
def updatePost(postId, title, content):
    try:
        post = getPostById(postId)
        post.title = title
        post.content = content
        post.html_content = markdown(content)
        db.session.commit()
        return post
    except:
        return

def deletePost(postId):
    try:
        post = getPostById(postId)
        db.session.delete(post)
        db.session.commit()
    except:
        return
    
