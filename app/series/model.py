from app.posts.model import Post
from app import db

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Post', backref='series', lazy=True, order_by='Post.published_at')

    def toDictionary(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'posts' : self.posts
        }