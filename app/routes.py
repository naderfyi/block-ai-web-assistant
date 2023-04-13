from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_cors import CORS
from flask_login import login_user, logout_user, login_required, current_user
from .db import db
from .models import User, ActivityLog
from .utils import authenticate_user, create_user, call_gpt4_api, log_user_activity

main = Blueprint('main', __name__)
CORS(main)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = authenticate_user(email, password)
        if user:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = create_user(email, password)
        if user:
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('main.login'))
        else:
            flash('Registration failed. Please try again.', 'danger')

    return render_template('register.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/api/gpt4', methods=['POST'])
@login_required
def gpt4_api_call():
    prompt = request.form.get('prompt')
    environment = request.form.get('environment')
    user_id = current_user.id

    response = call_gpt4_api(prompt, environment)

    log_user_activity(user_id, prompt, response)

    return jsonify(response)

@main.route('/api/user_activity', methods=['GET'])
@login_required
def get_user_activity():
    user_id = current_user.id
    activities = ActivityLog.query.filter_by(user_id=user_id).all()

    return jsonify([activity.to_dict() for activity in activities])
