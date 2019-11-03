from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import Required, Email


class SignupForm(Form):
    
    name = TextField('Your name', validators=[Required()], _name='nama')
    password = TextField('Your favorite password', validators=[Required()], _name='password')
    email = TextField('Your email address', validators=[Email()], _name='email')
    birthday = DateField('Your birthday', _name='birthday')

    # a_float = FloatField(u'A floating point number', _name='float')
    # a_decimal = DecimalField(u'Another floating point number', _name='desimal')
    # a_integer = IntegerField(u'An integer', _name='birthdaangka')

    # now = DateTimeField(u'Current time',
    #                     description='...for no particular reason', _name='tanggal_lahir')
    # sample_file = FileField(u'Your favorite file', _name='foto')
    # eula = BooleanField(u'I did not read the terms and conditions',
    #                     validators=[Required('You must agree to not agree!')], 
    #                     _name='setuju')

    submit = SubmitField(u'Signup', _name='signup')

class LoginFom(Form):
    name = TextField('Your name', validators=[Required()], _name='nama')
    password = TextField('Your favorite password', validators=[Required()], _name='password')
    submit = SubmitField('Login', _name='login')