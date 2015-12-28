from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    name = StringField('Ваше имя', validators=[Required()])
    submit = SubmitField('Зайти в чат')
