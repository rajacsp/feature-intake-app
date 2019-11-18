from flasktasks import db
from flasktasks.models import Tag, Category, Task, Color, User, Benefit

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

def create_benefit_types():
    benefit1 = Benefit("Increase revenue")
    benefit2 = Benefit("Increase number of customers")
    benefit3 = Benefit("Optimize/Reduce cost")
    benefit4 = Benefit("Increase customer retention")
    
    db.session.add(benefit1)
    db.session.add(benefit2)
    db.session.add(benefit3)
    db.session.add(benefit4)

    db.session.commit()

def create_categories():
    category1 = Category("Front End", 'UI Work', 1)
    category2 = Category("Back End", 'Backend Work', 2)

    db.session.add(category1)
    db.session.add(category2)

    db.session.commit()

def create_tasks():
    for i in range(1, 3):
        task1 = Task("First Task", "Outcome", "Some useful description", i)
        task2 = Task("Second Task", "Outcome", "Some useful description", i)

        db.session.add(task1)
        db.session.add(task2)

    db.session.commit()

def run_seed():
    
    print("Creating Users...")
    create_users()

    print("Creating Benefits...")
    create_benefit_types()

    print("Creating Tags...")
    create_tags()

    print("Creating Categories...")
    create_categories()

    print("Creating Tasks...")
    create_tasks()
