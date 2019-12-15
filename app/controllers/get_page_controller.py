from app import app
from bs4 import BeautifulSoup
import requests

def get_page_controller(form):
  page_url = form.url.data

  page = requests.get(page_url)
  soup = BeautifulSoup(page.text, 'html.parser')

  for script in soup(["script", "style", "meta", "noscript"]): # remove all javascript and stylesheet code
    script.extract()

  text = soup.get_text()

  # print(soup.prettify())
  print(text)