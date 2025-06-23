# app.py
# Import necessary modules from Flask and SQLAlchemy
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app instance
app = Flask(__name__)

# Configure the SQLite database file (saved as data.db in the project folder)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# Create a database object using SQLAlchemy
db = SQLAlchemy(app)

# Define a database model (table) named 'Employee'
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each record
    name = db.Column(db.String(100), nullable=False)  # Name field that cannot be empty

# Create the database and table if they don’t already exist
with app.app_context():
    db.create_all()

# Define the home route to show the HTML form and handle submissions
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # If the form was submitted
        name = request.form['name']  # Get the name from the form input
        
        if name:  # Check if name is not empty
            new_employee = Employee(name=name)  # Create a new Employee object
            db.session.add(new_employee)  # Add it to the session
            db.session.commit()  # Save it to the database
            return redirect('/')  # Redirect to home page after submission

    # If GET request, just render the form
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
