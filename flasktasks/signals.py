from blinker import Namespace


flasktasks_signals = Namespace()
task_created = flasktasks_signals.signal('task-created')
category_created = flasktasks_signals.signal('category-created')
