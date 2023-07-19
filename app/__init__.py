from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import sys
import os

# gets parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

#imports in parent directory i.e. config
from config import Config


db = SQLAlchemy()

post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    from app.main.routes import routesBlueprint
    app.register_blueprint(routesBlueprint)

    return app