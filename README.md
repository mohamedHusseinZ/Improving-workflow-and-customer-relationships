# Improving-workflow-and-customer-relationships
Improving Workflow and Customer Relationships
This is a Flask-based application designed to streamline business operations by managing customers, tasks, interactions, and feedback. The app features user authentication and allows for the creation and retrieval of customers, tasks, interactions, and feedback records.

Features
User Authentication: Register and log in users with JWT-based authentication.
Customer Management: Create and retrieve customer data by email.
Task Management: Add tasks associated with customers and retrieve tasks for specific customers.
Interaction Logging: Record and retrieve customer interactions.
Customer Feedback: Add and view customer feedback.
Technology Stack
Flask: Web framework
Flask-JWT-Extended: For JWT-based authentication
SQLAlchemy: ORM for database interactions
PostgreSQL: Database
Python 3.11
Installation
Prerequisites
Python 3.11+
PostgreSQL
Flask and other dependencies from requirements.txt
Step 1: Clone the repository
bash
Copy code
git clone https://github.com/mohamedHusseinZ/Improving-workflow-and-customer-relationships.git
cd Improving-workflow-and-customer-relationships
Step 2: Install the required dependencies
bash
Copy code
pip install -r requirements.txt
Step 3: Set up PostgreSQL
Create a PostgreSQL database and update your configuration in the Config class inside config.py with the database URL.

Step 4: Run Database Migrations
bash
Copy code
flask db upgrade
Step 5: Run the Application
bash
Copy code
python app.py
The app will run on http://127.0.0.1:5000/ by default.

API Endpoints
User Authentication
POST /register: Register a new user.

Request body: {"username": "user", "password": "pass"}
POST /login: Log in a user and get an access token.

Request body: {"username": "user", "password": "pass"}
Customer Management
POST /create_customer: Create a new customer. Requires a JWT token.

Request body: {"name": "John Doe", "email": "john@example.com"}
GET /get_customer/<email>: Retrieve customer details by email. Requires a JWT token.

Task Management
POST /create_task: Create a new task for a customer. Requires a JWT token.

Request body: {"description": "New Task", "status": "open", "customer_id": 1}
GET /get_tasks/<customer_id>: Retrieve all tasks for a specific customer. Requires a JWT token.

Interaction Management
POST /add_interaction: Add an interaction for a customer. Requires a JWT token.

Request body: {"customer_id": 1, "notes": "Had a great meeting"}
GET /get_interactions/<customer_id>: Retrieve all interactions for a customer. Requires a JWT token.

Feedback Management
POST /add_feedback: Add feedback for a customer. Requires a JWT token.

Request body: {"customer_id": 1, "feedback_text": "Very satisfied with the service"}
GET /get_feedback/<customer_id>: Retrieve all feedback for a customer. Requires a JWT token.

Protected Route Example
GET /protected: A test route that requires a valid JWT token to access.
License
This project is licensed under the MIT License.