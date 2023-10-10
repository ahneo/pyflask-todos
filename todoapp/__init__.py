from flask import Flask, jsonify
from flask_pymongo import PyMongo

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = ''
    mongo = PyMongo(app)
    todos = mongo.db.todos

    @app.route('/')
    def index():
        saved_todos = []
        cursor = todos.find()
        for i in cursor:
            saved_todos.append({
                'id': str(i['_id']),
                'todo': i['todo']
            })
        print("testing",saved_todos)
        return jsonify({'todos': saved_todos})

    return app