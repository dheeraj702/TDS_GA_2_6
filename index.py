from flask import Flask, request, jsonify
from flask_cors import CORS
import json

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Load the marks data from the file
with open('q-vercel-python.json', 'r') as f:
    data = json.load(f)

# Function to get marks based on student names
def get_marks(names):
    marks = []
    for name in names:
        student_data = next((student for student in data if student['name'] == name), None)
        marks.append(student_data['marks'] if student_data else None)
    return marks

# API endpoint to fetch marks
@app.route('/api', methods=['GET'])
def api():
    names = request.args.getlist('name')  # Get the list of names from query params
    marks = get_marks(names)
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
