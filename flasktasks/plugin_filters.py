from flask import Markup
from flasktasks import app
from flasktasks.plugins import dispatch


@app.template_filter('html_dispatch')
def html_dispatch(category, function):
    values = dispatch(function, category)
    return Markup(''.join(values))
