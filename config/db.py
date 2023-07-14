import pymongo

def getClient(username, password, db_name):
    return pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.wctesmk.mongodb.net/?retryWrites=true&w=majority")
