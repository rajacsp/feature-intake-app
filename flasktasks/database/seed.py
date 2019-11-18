from flasktasks import db
from flasktasks.models import Tag, Mission, Task, Color, User

def create_users():
    user1 = User("raja", "test", 1)
    user2 = User("gautam", "test", 2)
    
    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

def create_tags():
    tag1 = Tag("Work", Color.BLUE)
    tag2 = Tag("College", Color.RED)
    tag3 = Tag("Side Project", Color.GREEN)
    
    db.session.add(tag1)
    db.session.add(tag2)
    db.session.add(tag3)

    db.session.commit()

def create_categories():
    mission1 = Mission("Finish Stuff", 'Just finish some stuff', 1)
    mission2 = Mission("Whatever Class", 'Accomplish that impossible goal', 2)
    mission3 = Mission("Second Release", 'Pretend to be productive', 3)

    db.session.add(mission1)
    db.session.add(mission2)
    db.session.add(mission3)

    db.session.commit()

def create_tasks():
    for i in range(1, 4):
        task1 = Task("First Task", "Some useful description", i)
        task2 = Task("Second Task", "Some useful description", i)
        task3 = Task("Third Task", "Some useful description", i)

        db.session.add(task1)
        db.session.add(task2)
        db.session.add(task3)

    db.session.commit()

def run_seed():
    
    print("Creating Users...")
    create_users()

    print("Creating Tags...")
    create_tags()

    print("Creating Categories...")
    create_categories()

    print("Creating Tasks...")
    create_tasks()
