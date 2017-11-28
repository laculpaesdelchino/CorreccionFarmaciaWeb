from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

#----Formularios Flask para usar ventanas de dialogo para meter info----

class LoginForm(FlaskForm):
    usuario = StringField('Nombre de usuario', validators=[Required()])
    password = PasswordField('Contraseña', validators=[Required()])
    enviar = SubmitField('Ingresar')

class ProductoForm(FlaskForm):
    producto = StringField('Ingrese el producto que desea Buscar ', validators=[Required()])
    enviar = SubmitField('Buscar')

class ClienteForm(FlaskForm):
    cliente = StringField('Ingrese el nombre que desea Buscar ', validators=[Required()])
    enviar = SubmitField('Buscar')

class CrearUsuario(FlaskForm):
	usuarioNuevo = StringField('Nombre de usuario', validators=[Required()])
	passwordNuevo = PasswordField('Contraseña ', validators=[Required()])
	enviar = SubmitField('Enviar')