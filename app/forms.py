from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, Length


class userForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    apellido = StringField('Apellido', validators=[DataRequired(), Length(max=50)])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    ID = IntegerField('Número de Identificación', validators=[DataRequired()])
    direccion = StringField('Dirección', validators=[DataRequired()])
    codigoPostal = IntegerField('Codigó Postal', validators=[DataRequired()])


class loginForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    apellido = StringField('Apellido', validators=[DataRequired(), Length(max=50)])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
