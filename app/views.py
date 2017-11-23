from flask import Flask, render_template
from app import app, db

@app.route('/')
@app.route('/index')
def index():
  query = 'select username from User'
  result = db.engine.execute(query)
  usernames = []
  for row in result:
    usernames.append(row[0])
  return render_template('index.pug',
                        usernames = usernames)
@app.route('/cards')
def cards():
  return render_template('cards.pug')

@app.route('/yourCollection')
def yourCollection():
  return render_template('yourCollection.pug')

@app.route('/cardGenerator')
def cardGenerator():
  return render_template('cardGenerator.pug')

@app.route('/about')
def about():
  return render_template('about.pug')

@app.route('/contact')
def contact():
  return render_template('contact.pug')
@app.route('/login')
def login():
  return render_template('login.pug')

@app.route('/logout')
def logout():
  return render_template('index.pug')



