from app import app
from flask import render_template

from app.forms import GetPageForm
from app.controllers.get_page_controller import get_page_controller

@app.route('/', methods=('GET', 'POST'))
def get_page(): 
  return get_page_controller()