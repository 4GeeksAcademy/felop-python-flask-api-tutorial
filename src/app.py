# Add the jsonify method to your Flask import
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)
# Suppose you have your data in the variable named some_data
todos = [{ "label": "My first task", "done": False },
         { "label": "My second task", "done": False }
         ]

@app.route('/todos', methods=['GET'])
def get_todos():
    # You can convert that variable into a json string like this
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():

    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(dict(request_body))
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if position < 0 or position >= len(todos):
        return jsonify({"error":"Invalid position"}),400

    todos.pop(position)
    return jsonify(todos) 

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)