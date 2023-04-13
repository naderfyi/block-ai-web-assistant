import os
from firebase_admin import credentials, firestore, initialize_app

# Load the Firebase private key JSON file
private_key_file = os.path.join(os.path.dirname(__file__), 'secrets', 'firebase-private-key.json')

# Initialize the Firebase app
cred = credentials.Certificate(private_key_file)
firebase_app = initialize_app(cred)

# Initialize Firestore
db = firestore.client()
