from app import db
from app.tags.model import Tag

def createTag(name):
    tag = Tag(name=name)
    db.session.add(tag)

    db.session.commit()
    return tag

def getAllTags():
    return Tag.query_all()

def getTagById(tagId):
    return Tag.query.