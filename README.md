# BlockAI Assistant Tool

The BlockAI Assistant Tool is a web application designed to help non-programmers interact with the GPT-4 API for research purposes and low-code development in the web3 space. The tool features user authentication, role-based access control, a user-friendly interface, and activity tracking.

## Technologies

- Backend: Flask
- Frontend: React
- Database: Firestore
- Authentication: Firebase Authentication
- GPT API Integration: OpenAI Python library

## Features

- User Authentication & Authorization
- API Integration with GPT-4
- User Interface (UI)
- User Activity Tracking
- Backend Server
- Database

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/web3-assistant-tool.git
cd web3-assistant-tool
```

2. Set up a virtual environment and install required packages:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Set up Firebase:
- Create a new Firebase project.
- Set up Realtime Database or Firestore.
- Set up Firebase Authentication.
- Download your Firebase project's configuration file and place it in the appropriate directory.

4. Configure environment variables:
- Create a .env file in the root directory and add the following variables:
 - FLASK_APP: The entry point of your Flask application (e.g., app.py).
 - FLASK_ENV: The environment in which your app is running (e.g., development).
 - GPT_API_KEY: Your GPT-4 API key.
 - FIREBASE_CONFIG: Path to your Firebase configuration file.

5. Run the application:
```bash
flask run
```
