from flask import Blueprint, render_template, request, redirect, url_for
from .models import Task
from . import db

routes = Blueprint('routes', __name__)

@routes.route('/')
def view_tasks():
    tasks = Task.query.all()
    return render_template('view.html', tasks=tasks)

@routes.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('routes.view_tasks'))  # Use blueprint name
    return render_template('add.html')

@routes.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        db.session.commit()
        return redirect(url_for('routes.view_tasks'))  # Use blueprint name
    return render_template('update.html', task=task)

@routes.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('routes.view_tasks'))  # Use blueprint name

