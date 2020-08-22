#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:33:02 2020

@author: fahimtalukder
"""

from flask import Flask, render_template
from forms import LoginForm

app = Flask(__name__)

app.config ['SECRET_KEY'] = 'fd3313cc5d1b034d2e3402952bf081cd'

posts = [
      {
       'title' : 'afasf dvsd',
       'author' : 'abc',
       'content' : 'first aritcle',
       'date_posted' : 'May 18, 2020',
       
       },
       {
       'title' : 'ab author',
       'author' : 'article dui',
       'content' : 'secound aritcle',
       'date_posted' : 'june 18, 2020',
       
       }
      ]

@app.route('/')
@app.route("/home")
def home():
   
    return render_template('home.html')

@app.route("/article")
def article():
    
   
    return render_template('articles.html', posts = posts)


@app.route("/Login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
    
     
    
    
    
if __name__ == '__main__':
    app.run(debug=True) 