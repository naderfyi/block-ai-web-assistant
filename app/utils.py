from dotenv import load_dotenv
from os import getenv
import openai
from .models import User, ActivityLog
from datetime import datetime
from .db import db

# Load environment variables from .env file
load_dotenv()

# Retrieve GPT-4 API key from environment variables
GPT4_API_KEY = getenv("GPT4_API_KEY")

# Add this function to the utils.py file
def create_user(email, password):
    try:
        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    except Exception as e:
        print(f"Error creating user: {e}")
        return None

def authenticate_user(email, password):
    user = User.get_by_email(email)
    if user and user.password == password:
        return user
    return None

def call_gpt4_api(prompt, environment):
    # Set up OpenAI API client
    openai.api_key = GPT4_API_KEY

    # Customize the API call based on the environment and other parameters
    api_params = {
        'engine': 'text-davinci-002',
        'prompt': prompt,
        'max_tokens': 100,
        'temperature': 0.7
    }

    response = openai.Completion.create(**api_params)

    # Extract and return the generated text from the API response
    return response.choices[0].text.strip()

def log_user_activity(user_id, prompt, response):
    try:
        activity_log = ActivityLog(user_id=user_id, prompt=prompt, response=response)
        db.session.add(activity_log)
        db.session.commit()
    except Exception as e:
        print(f"Error logging user activity: {e}")