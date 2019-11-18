from flask import render_template, request, redirect, url_for, abort, jsonify
from collections import defaultdict
from flasktasks import app, db
from flasktasks.models import Category, Task, Status, Tag, Color, LogEntry, User, Benefit
from flasktasks.signals import task_created, category_created 


@app.route('/')
def index():
    categories = Category.query.all()
    benefits = Benefit.query.all()
    return render_template('home.html', categories=categories, benefits = benefits)

@app.route('/login')
def login_page():
    return render_template('login.html')


def is_user_available(email, password):

    CUser = db.session.query(User).filter(User.email == email).filter(User.password == password).first()

    #print(CUser)

    if(CUser):
        return True

    return False

@app.route('/login', methods=['POST'])
def login():

    email = request.form.get('email')
    password = request.form.get('password')

    #print(email, password)

    if(is_user_available(email, password)):
        return render_template('loggedin.html')

    return render_template('login_failed.html')

@app.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template('category/index.html', categories=categories)

@app.route('/categories/new', methods=['POST', 'GET'])
def new_category():
    if request.method == 'POST':
        category = Category(request.form.get('title'),
                          request.form.get('description'),
                          request.form.get('tag_id'))
        db.session.add(category)
        db.session.commit()
        category_created.send(category)
        return redirect(url_for('categories'))
    else:
        tags = Tag.query.all()
        return render_template('category/new.html', tags=tags)

@app.route('/tasks')
def tasks():
    category = None
    if request.args.get('category_id'):
        category = Category.query.get_or_404(request.args.get('category_id'))
        tasks = Task.query.filter_by(category_id=category.id).all()
    else:
        tasks = Task.query.all()

    tasks_by_status = defaultdict(list)
    for task in tasks:
        status = Status(task.status).name 
        tasks_by_status[status].append(task)
    return render_template('task/index.html', tasks=tasks_by_status,
                           category=category)

@app.route('/tasks/new', methods=['POST', 'GET'])
def new_task():
    if request.method == 'POST':
        task = Task(request.form.get('title'),
                    request.form.get('outcome'),
                    request.form.get('description'),
                    request.form.get('category_id'))
        db.session.add(task)
        db.session.commit()
        task_created.send(task)
        return redirect(url_for('tasks'))
    else:
        categories = Category.query.all()
        return render_template('task/new.html', categories=categories)


@app.route('/tasks/<int:task_id>', methods=['POST'])
def update_task(task_id):

    task = Task.query.get_or_404(task_id)
    try:
        task.title = request.form.get('title')
        task.description = request.form.get('description')
    except KeyError:
        abort(400)

    db.session.add(task)
    db.session.commit()
    return redirect(url_for('tasks'))
    

@app.route('/tasks/<int:task_id>')
def task(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('task/task.html', task=task)

@app.route('/tasks/<int:task_id>/set_status/<status>')
def set_status(task_id, status):
    task = Task.query.get_or_404(task_id)
    try:
        task.status = Status[status.upper()].value
    except KeyError:
        abort(400)

    db.session.add(task)
    db.session.commit()
    return redirect(url_for('tasks'))

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return url_for('tasks')
    
@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return url_for('categories')

@app.route('/tags/new', methods=['POST', 'GET'])
def new_tag():
    if request.method == 'POST':
        try:
            color = Color(int(request.form.get('color_id')))
        except ValueError:
            abort(400)
        tag = Tag(request.form.get('name'), color)
        db.session.add(tag)
        db.session.commit()
        return redirect(url_for('categories'))
    else:
        colors = { color.name: color.value for color in Color }
        return render_template('tags/new.html', colors=colors)


@app.route('/log')
def log():
    log_entries = LogEntry.query.all()
    return render_template('log.html', log_entries=log_entries)
