# json_app.py
# This script creates a dictionary, converts it to JSON format, and prints it

import json  # Import the json module

# Create a dictionary with key-value pairs
data = {
    'name': 'Tien Tang',
    'age': 18,
    'city': 'Seattle, WA',
    'interests': ['Powerlifting', 'Fishing', 'Cars'],
    'is_student': True
}

# Convert the dictionary to a JSON string
json_string = json.dumps(data, indent=4)

# Print the JSON string
print(json_string)

# Optional: Save the JSON string to a file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
