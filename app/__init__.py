from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import Config
from app.database.db import db
from app.posts.controller import postsBlueprint
from app.main.routes import routesBlueprint

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "big key dsdksndsjnksdn"
    app.config['WTF_CSRF_ENABLED'] = False
    app.config.from_object(Config)

    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    '''
    post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
    )
    '''
    
    
    app.register_blueprint(routesBlueprint)
    app.register_blueprint(postsBlueprint)

    return app