#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:13:47 2020

@author: fahimtalukder
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email
 
    class LoginForm(FlaskForm):
        
        email = StringField('Email',
                            validators = [DataRequired(), Email()]
        password = PasswordField('Password', validators = [DataRequired()]
        remember = BooleanField('Remember Me')
        submit = SubmitField('Log in', )