import datetime
from app import post_tags
from app.tags.model import Tag
from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    htmlContent = db.Content(db.Text, nullable=False)
    #tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def toDictionary(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'html_content': self.htmlContent
        }