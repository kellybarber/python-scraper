import os

class Config(object):
  SECRET_KEY            = "6b043c37-0aa4-421c-8050-409583cc14ba"
  BASE_DIR              = os.path.abspath(os.path.dirname(__file__))
  THREADS_PER_PAGE      = 2
  CSRF_ENABLED          = True
  CSRF_SESSION_KEY      = "a253324c-4cfa-41ce-b025-6c85eed48598"
  DEBUG                 = True
  TEMPLATES_AUTO_RELOAD = True