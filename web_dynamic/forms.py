#!/usr/bin/python3
""" signup form class """

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Email, EqualTo, length

class SignUpForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(), length(max=128)])
    username = StringField('Username', validators=[DataRequired(), length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=4, max=14)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Signup')
    
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(), length(max=128)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=4, max=20)])
    submit = SubmitField('Login')
    
class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current password', validators=[DataRequired(), length(min=4, max=20)], render_kw={"id": "current_password"})
    new_password = PasswordField('New password', validators=[DataRequired(), length(min=4, max=20)], render_kw={"id": "new_password"})
    confirm_new_password = PasswordField('Confirm new Password', validators=[DataRequired(), EqualTo('new_password')], render_kw={"id": "confirm_new_password"})
    submit = SubmitField('Change')
    
class MakeAdmin(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=2, max=20)])
    submit = SubmitField('Make admin')

class TaleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), length(min=2, max=128)])
    content = TextAreaField('Content', validators=[DataRequired(), length(min=2, max=1000)])
    submit = SubmitField('Create')    

class EditProfileForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired(), length(min=2, max=20)])
    about = TextAreaField('About', validators=[length(min=2, max=256)])
    submit = SubmitField('Update')
    
class EditTaleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), length(min=2, max=124)])
    content = TextAreaField('Content', validators=[length(min=2, max=2000)])
    submit = SubmitField('Update')

class CollectionForm(FlaskForm):
    """Form for creating or editing a collection"""
    title = StringField('Title', validators=[DataRequired(), length(min=2, max=128)])
    description = TextAreaField('Description', validators=[length(max=124)], render_kw={"rows": 4})
    submit = SubmitField('Create')

class AddTalesToCollectionForm(FlaskForm):
    """Form for adding tales to a collection"""
    tales = SelectMultipleField('Tales', coerce=str)
    submit = SubmitField('Add Tales')
    