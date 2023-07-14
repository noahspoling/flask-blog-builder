from config.db import getClient
from gridfs import GridFS
from dotenv import load_dotenv
import os


def uploadDocument(path):
    try:
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        db_name = os.getenv("DB_NAME")

        client = getClient(username, password, db_name)  # Get MongoDB client
        db = client.test  # Use your database
        fs = GridFS(db)

        with open(path, 'rb') as f:
            filename = os.path.basename(path)
            file_id = fs.put(f, filename=filename)

        return file_id
    except:
        print(f'Upload failed...\n')

def getDocuments( page, documents_per_page = 10 ):
    try:
        client = getClient()
        db = client.test
        fs = GridFS(db)

        # Skipping the documents as per the page number
        skip = documents_per_page * (page - 1)

        files = fs.find().skip(skip).limit(documents_per_page)

        file_list = []
        for file in files:
            file_list.append({"filename": file.filename, "length": file.length})

        return file_list

    except:
        print(f"An error occurred \n")
        return
    
def getDocumentById(file_id):
    client = getClient()
    db = client.test
    fs = GridFS(db)

    file = fs.get(file_id)
    content = file.read().decode('utf-8')

    return content