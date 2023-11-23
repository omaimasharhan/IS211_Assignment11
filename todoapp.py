from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todo_list = [
    {'task': 'Buy groceries', 'email': 'example@email.com', 'priority': 'High'},
    {'task': 'Finish assignment', 'email': 'another@example.com', 'priority': 'Medium'},

]

@app.route('/')
def view_todo_list():
    return render_template('todo_list.html', todo_list=todo_list)

@app.route('/submit', methods=['POST'])
def submit_todo_item():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    todo_list.append({'task': task, 'email': email, 'priority': priority})
    return redirect(url_for('view_todo_list'))

@app.route('/clear', methods=['POST'])
def clear_todo_list():
    todo_list.clear()
    return redirect(url_for('view_todo_list'))

@app.route('/delete/<int:item_index>', methods=['POST'])
def delete_todo_item(item_index):
    if 0 <= item_index < len(todo_list):
        del todo_list[item_index]
    return redirect(url_for('view_todo_list'))

if __name__ == '__main__':
    app.run(debug=True)
