# service.py

from datetime import datetime
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from model import db, User, Customer, Task, Interaction, Feedback

def register_user(username, password):
    if User.query.filter_by(username=username).first():
        raise ValueError("User already exists")
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity={'username': user.username})
        return access_token
    else:
        raise ValueError("Invalid credentials")

def create_customer(name, email):
    customer = Customer(name=name, email=email)
    db.session.add(customer)
    db.session.commit()

def create_task(description, status, customer_id):
    task = Task(description=description, status=status, customer_id=customer_id)
    db.session.add(task)
    db.session.commit()

def add_interaction(customer_id, notes):
    interaction = Interaction(date=datetime.now(), notes=notes, customer_id=customer_id)
    db.session.add(interaction)
    db.session.commit()

def add_feedback(customer_id, feedback_text):
    feedback = Feedback(customer_id=customer_id, feedback_text=feedback_text, date=datetime.now())
    db.session.add(feedback)
    db.session.commit()

def get_customer_by_email(email):
    return Customer.query.filter_by(email=email).first()

def get_tasks_for_customer(customer_id):
    return Task.query.filter_by(customer_id=customer_id).all()

def get_interactions_for_customer(customer_id):
    return Interaction.query.filter_by(customer_id=customer_id).all()

def get_feedback_for_customer(customer_id):
    return Feedback.query.filter_by(customer_id=customer_id).all()
