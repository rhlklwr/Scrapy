import firebase_admin
from firebase_admin import credentials, firestore


class FirestoreDatabase:

    def __init__(self, key='./ServiceAccountKey.json'):
        # Authentication with Firebase
        if not firebase_admin._apps:
            self.cred = credentials.Certificate(key)
            self.app = firebase_admin.initialize_app(self.cred)

    def __enter__(self):
        # Instantiate Firestore class
        self.db = firestore.client()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print('Error')
        else:
            print("Done")
            # self.db.batch.commit()

