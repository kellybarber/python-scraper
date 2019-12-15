from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired

class GetPageForm(FlaskForm):
  url = StringField('URL', [ 
    URL(message=('Not a valid url')),
    DataRequired() 
  ])
  submit = SubmitField('Submit')