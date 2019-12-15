from app import app
from flask import render_template, request
from bs4 import BeautifulSoup
from app.forms import GetPageForm

import requests
import string

def get_page_controller():
  form = GetPageForm()
  page_url = form.url.data

  page = requests.get(page_url)
  soup = BeautifulSoup(page.text, 'html.parser')

  for script in soup(["script", "style", "meta", "noscript"]): # remove all javascript and stylesheet code
    script.extract()

  text         = soup.get_text()
  cleaned_text = text.translate(string.punctuation)
  text_array   = cleaned_text.lower().split()

  word_count = [
    { 'title' : 'We', 'count': text_array.count('we') },
    { 'title' : 'You', 'count': text_array.count('you') }
  ]

  return render_template('index.html', form=form, word_count=word_count)