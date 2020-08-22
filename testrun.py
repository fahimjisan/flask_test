#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:33:02 2020

@author: fahimtalukder
"""

from flask import Flask, render_template, request, session, redirect, url_for

class User:
    def __init__ (self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        
    def __repr__ (self):
        return f'<User: {self.username}>'
        
users = []
users.append(User(id=1, username = 'fahim', password = 'pass'))
users.append(User(id=1, username = 'ruthwik', password = 'word'))
users.append(User(id=1, username = 'abc', password = 'defg'))


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route("/profile")
def profile():
    return render_template('profile.html')



