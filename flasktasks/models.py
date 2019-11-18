from flasktasks import db
from enum import Enum
from time import strftime


class Status(Enum):
    PROPOSED = 1
    MANAGER_APPROVED = 2
    TO_DO = 3
    DOING = 4
    DONE = 5

class Color(Enum):
    GREY = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    RED = 5

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    description = db.Column(db.String(140))
    status = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, title, description, category_id):
        self.title = title
        self.description = description
        self.status = Status.PROPOSED.value
        self.category_id = category_id

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(210))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    tasks = db.relationship('Task', backref='category', lazy='dynamic')

    def __init__(self, title, description, tag_id):
        self.title = title
        self.description = description
        self.tag_id = tag_id

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    color = db.Column(db.Integer)
    categories = db.relationship('Category', backref='tag', lazy='dynamic')

    def __init__(self, name, color=Color.GREY):
        self.name = name
        self.color = color.value
    
    def style(self):
        color = Color(self.color)
        return "tagged tag-%s" % color.name.lower()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    role = db.Column(db.Integer)

    def __init__(self, name, password, role):
        self.email = name
        self.password = password
        self.role = role

class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(30))
    message = db.Column(db.String(140))

    def __init__(self, message):
        self.message = message
        self.timestamp = strftime("%d-%m-%Y %H:%M:%S")
