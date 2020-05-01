import firebase_admin
from firebase_admin import credentials, firestore

default_key = './ServiceAccountKey.json'
cred = credentials.Certificate(default_key)
default_app = firebase_admin.initialize_app(cred)

class FirestoreDatabase:

    def __init__(self, app=default_app):
        self.app = app

    def __enter__(self):
        # Instantiate Firestore class
        self.db = firestore.client()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print('Error')
        else:
            print("Done1")
            # self.db.batch.commit()


