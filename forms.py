from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FormaLogin(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='No dejar vacío, completar')])

    password = PasswordField('Password', validators=[DataRequired(message='No dejar vacío, completar')])

    enviar = SubmitField('Iniciar Sesión')
