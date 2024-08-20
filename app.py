# app.py

from flask import Flask, request, jsonify

from config import Config
from model import db, User, Customer, Task, Interaction, Feedback
from service import (
    register_user, login_user,
    create_customer, create_task, add_interaction, add_feedback,
    get_customer_by_email, get_tasks_for_customer, get_interactions_for_customer, get_feedback_for_customer
)
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Customer': Customer,
        'Task': Task,
        'Interaction': Interaction,
        'Feedback': Feedback
    }

# Registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        register_user(data['username'], data['password'])
        return jsonify({'message': 'User registered successfully'}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        access_token = login_user(data['username'], data['password'])
        return jsonify({'access_token': access_token}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 401

# Protected route example
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'message': f"Hello, {current_user['username']}!"}), 200

# Other routes
@app.route('/create_customer', methods=['POST'])
@jwt_required()
def create_customer_route():
    data = request.get_json()
    create_customer(data['name'], data['email'])
    return jsonify({'message': 'Customer created successfully'}), 201

@app.route('/create_task', methods=['POST'])
@jwt_required()
def create_task_route():
    data = request.get_json()
    create_task(data['description'], data['status'], data['customer_id'])
    return jsonify({'message': 'Task created successfully'}), 201

@app.route('/add_interaction', methods=['POST'])
@jwt_required()
def add_interaction_route():
    data = request.get_json()
    add_interaction(data['customer_id'], data['notes'])
    return jsonify({'message': 'Interaction added successfully'}), 201

@app.route('/add_feedback', methods=['POST'])
@jwt_required()
def add_feedback_route():
    data = request.get_json()
    add_feedback(data['customer_id'], data['feedback_text'])
    return jsonify({'message': 'Feedback added successfully'}), 201

@app.route('/get_customer/<email>', methods=['GET'])
@jwt_required()
def get_customer_route(email):
    customer = get_customer_by_email(email)
    if customer:
        return jsonify({'id': customer.id, 'name': customer.name, 'email': customer.email}), 200
    return jsonify({'message': 'Customer not found'}), 404

@app.route('/get_tasks/<customer_id>', methods=['GET'])
@jwt_required()
def get_tasks_route(customer_id):
    tasks = get_tasks_for_customer(customer_id)
    return jsonify([{'id': task.id, 'description': task.description, 'status': task.status} for task in tasks]), 200

@app.route('/get_interactions/<customer_id>', methods=['GET'])
@jwt_required()
def get_interactions_route(customer_id):
    interactions = get_interactions_for_customer(customer_id)
    return jsonify([{'id': interaction.id, 'date': interaction.date, 'notes': interaction.notes} for interaction in interactions]), 200

@app.route('/get_feedback/<customer_id>', methods=['GET'])
@jwt_required()
def get_feedback_route(customer_id):
    feedbacks = get_feedback_for_customer(customer_id)
    return jsonify([{'id': feedback.id, 'feedback_text': feedback.feedback_text, 'date': feedback.date} for feedback in feedbacks]), 200

if __name__ == '__main__':
    app.run(debug=True)
