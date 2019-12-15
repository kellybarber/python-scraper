from app import app
from flask import render_template, request

from app.forms import GetPageForm
from app.controllers.get_page_controller import get_page_controller

@app.route('/', methods=('GET', 'POST'))
def get_page():
    form = GetPageForm()
    get_page_controller(form)

    return render_template('index.html', form=form)