from google.cloud.firestore import DocumentReference
from .db import db

class User:
    def __init__(self, user_id, email, password, role):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.role = role

    def save(self):
        user_data = {
            'user_id': self.user_id,
            'email': self.email,
            'password': self.password,
            'role': self.role
        }
        db.collection('users').document(self.user_id).set(user_data)

    @staticmethod
    def get_by_email(email):
        users = db.collection('users').where('email', '==', email).stream()
        for user in users:
            return User.from_dict(user.to_dict())
        return None

    @staticmethod
    def from_dict(user_data):
        return User(user_data['user_id'], user_data['email'], user_data['password'], user_data['role'])

class ActivityLog:
    def __init__(self, user_id, timestamp, input_text, output_text):
        self.user_id = user_id
        self.timestamp = timestamp
        self.input_text = input_text
        self.output_text = output_text

    def save(self):
        activity_data = {
            'user_id': self.user_id,
            'timestamp': self.timestamp,
            'input_text': self.input_text,
            'output_text': self.output_text
        }
        db.collection('activity_logs').add(activity_data)

    @staticmethod
    def from_dict(activity_data):
        return ActivityLog(activity_data['user_id'], activity_data['timestamp'], activity_data['input_text'], activity_data['output_text'])

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'timestamp': self.timestamp,
            'input_text': self.input_text,
            'output_text': self.output_text
        }