# Import Flask and the function to load HTML templates
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the home page (URL: "/")
@app.route('/')
def home():
    # Render the home.html file from the templates folder
    return render_template('home.html')

# Define the route for the about page (URL: "/about")
@app.route('/about')
def about():
    # Render the about.html file
    return render_template('about.html')

# Define the route for the contact page (URL: "/contact")
@app.route('/contact')
def contact():
    # Render the contact.html file
    return render_template('contact.html')

# Run the app if this file is executed directly
if __name__ == '__main__':
    # Enable debug mode for automatic reloads during development
    app.run(debug=True)
