from flask import Flask, render_template, request, redirect

app = Flask(__name__)
to_do_list = []

@app.route('/', methods=['GET', 'POST'])
def view_to_do_list():
    error = None

    if request.method == 'POST':
        if 'action' in request.form:
            if request.form['action'] == 'clear':
                to_do_list.clear()
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
            return redirect('/')

    return render_template('todo_list.html', to_do_list=to_do_list, error=error)

if __name__ == '__main__':
    app.run(debug=True)
