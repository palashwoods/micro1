from flask import Flask, request, jsonify

app = Flask(__name__)

# Create an initial list of tasks for demonstration purposes
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Build a Microservice", "completed": False},
]

# Helper function to find a task by its ID
def find_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = find_task(task_id)
    if task:
        return jsonify(task)
    else:
        return jsonify(error="Task not found"), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' not in data:
        return jsonify(error="Title is required"), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = find_task(task_id)
    if not task:
        return jsonify(error="Task not found"), 404
    
    data = request.get_json()
    if 'title' in data:
        task['title'] = data['title']
    if 'completed' in data:
        task['completed'] = data['completed']
    
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = find_task(task_id)
    if not task:
        return jsonify(error="Task not found"), 404
    
    tasks.remove(task)
    return jsonify(message="Task deleted")

#if __name__ == '__main__':
 #  app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081)

