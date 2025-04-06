from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks')
def show_tasks():
    return render_template('tasks.html', tasks=tasks)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task')
    if task_name:
        tasks.append({'name': task_name, 'done': False})
    return redirect(url_for('show_tasks'))

@app.route('/done/<int:task_id>')
def mark_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
    return redirect(url_for('show_tasks'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('show_tasks'))

if __name__ == '__main__':
    app.run(debug=True)
