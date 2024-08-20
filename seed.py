from app import app
from model import db, User, Customer, Task, Interaction, Feedback
from datetime import datetime

def seed_database():
    with app.app_context():
        # Create sample users
        user1 = User(username='admin', password_hash='admin')  # Password will be hashed
        user1.set_password('admin')  # Set the hashed password
        user2 = User(username='user', password_hash='user')  # Password will be hashed
        user2.set_password('user')  # Set the hashed password

        db.session.add_all([user1, user2])
        db.session.commit()

        # Create sample customers
        customer1 = Customer(name='Alice Johnson', email='alice.johnson@example.com')
        customer2 = Customer(name='Bob Smith', email='bob.smith@example.com')
        
        db.session.add_all([customer1, customer2])
        db.session.commit()

        # Create sample tasks
        task1 = Task(description='Follow up with Alice', status='Pending', customer_id=customer1.id)
        task2 = Task(description='Prepare report for Bob', status='Completed', customer_id=customer2.id)
        
        db.session.add_all([task1, task2])
        db.session.commit()

        # Create sample interactions
        interaction1 = Interaction(date=datetime.now(), notes='Discussed project requirements with Alice.', customer_id=customer1.id)
        interaction2 = Interaction(date=datetime.now(), notes='Reviewed Bob’s feedback on the draft.', customer_id=customer2.id)
        
        db.session.add_all([interaction1, interaction2])
        db.session.commit()

        # Create sample feedback
        feedback1 = Feedback(customer_id=customer1.id, feedback_text='Great service and timely responses.', date=datetime.now())
        feedback2 = Feedback(customer_id=customer2.id, feedback_text='The report needs more detailed analysis.', date=datetime.now())
        
        db.session.add_all([feedback1, feedback2])
        db.session.commit()

        print("Database seeded successfully.")

if __name__ == '__main__':
    seed_database()
