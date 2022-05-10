from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class Pitch(FlaskForm):
  title = StringField('Enter the Title', validators=[DataRequired()])
  description= TextAreaField('Give brief description',validators=[DataRequired()])
  submit = SubmitField('Submit')