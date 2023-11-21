from flask import Flask, render_template, request, redirect

app = Flask(__name__)
to_do_list = []

@app.route('/', methods=['GET', 'POST'])
def view_to_do_list():
    if request.method == 'POST':
        if request.form['action'] == 'clear':
            to_do_list.clear()
        else:
            task = request.form['task']
            email = request.form['email']
            priority = request.form['priority']

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

    return render_template('todo_list.html', to_do_list=to_do_list)

if __name__ == '__main__':
    app.run()
