from flask import Flask, render_template, request, redirect

app = Flask(__name__)
to_do_list = []

def write_tasks_to_file(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task[0]}, {task[1]}, {task[2]}\n")

# Function to read tasks from file
def read_tasks_from_file():
    to_do_list.clear()
    with open('tasks.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            task_data = line.strip().split(', ')
            to_do_list.append((task_data[0], task_data[1], task_data[2]))

# Read tasks from file when the app starts
read_tasks_from_file()

@app.route('/', methods=['GET', 'POST'])
def view_to_do_list():
    error = None

    if request.method == 'POST':
        if 'clear_button' in request.form:
            to_do_list.clear()
            write_tasks_to_file(to_do_list)
            return redirect('/')

        task = request.form.get('task')
        email = request.form.get('email')
        priority = request.form.get('priority')

        if not task.strip():
            error = 'Task is empty.'
        elif not email.strip() or '@' not in email:
            error = 'Invalid email format.'
        elif priority not in ('Low', 'Medium', 'High'):
            error = 'Invalid priority choice.'
        else:
            to_do_list.append((task, email, priority))
            write_tasks_to_file(to_do_list)
            return redirect('/')

    return render_template('todo_list.html', to_do_list=to_do_list, error=error)

@app.route('/clear', methods=['POST'])
def clear_to_do_list():
    to_do_list.clear()
    write_tasks_to_file(to_do_list)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
