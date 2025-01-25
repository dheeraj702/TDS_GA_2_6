from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

with open('q-vercel-python.json', 'r') as f:
    data = json.load(f)

def get_marks(names):
    marks = []
    for name in names:
        student_data = next((student for student in data if student['name'] == name), None)
        marks.append(student_data['marks'] if student_data else None)
    return marks

@app.route('/api', methods=['GET'])
def api():
    names = request.args.getlist('name')
    marks = get_marks(names)
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
