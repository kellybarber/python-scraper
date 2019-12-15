from app import app
from flask import render_template, redirect, url_for

import logging
from logging.handlers import RotatingFileHandler

from app.forms import GetPageForm

@app.route('/', methods=('GET', 'POST'))
def get_page():
    form = GetPageForm()
    
    app.logger.info(form)

    return render_template('index.html', form=form)