# app.py
from flask import Flask, request, jsonify
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

swagger = Swagger(app, template_file='RESTful.yaml')

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify([]), 200

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    return jsonify({'message': 'Course created', 'course': data}), 201

@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.json
    return jsonify({'message': 'teacher created', 'teacher': data}), 201

@app.route('/courses/1', methods=['PUT'])
def update_course():
    data = request.json
    return jsonify({'message': 'course updated', 'course': data}), 200


if __name__ == '__main__':
    app.run(debug=True)
