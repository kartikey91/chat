#!/usr/bin/env python
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///msgs.sqlite3'
app.config['SECRET_KEY'] = 'random string'

db = SQLAlchemy(app)

class msgs(db.Model):
   id = db.Column('msg_id', db.Integer, primary_key = True)
   msg_from = db.Column(db.String(100))
   msg_to = db.Column(db.String(50))
   msg = db.Column(db.String(200)) 

   def __init__(self, msg_from, msg_to, msg):
      self.msg_from = msg_from
      self.msg_to = msg_to
      self.msg = msg

@app.route('/new/<username>', methods = ['GET', 'POST'])
def new(username):
   # if request.method == 'POST':
   #    if not request.form['name'] or not request.form['city'] or not request.form['addr']:
   #       flash('Please enter all the fields', 'error')
   #    else:
   #       student = students(request.form['name'], request.form['city'],
   #          request.form['addr'], request.form['pin'])
         
   #       db.session.add(student)
   #       db.session.commit()
   #       flash('Record was successfully added')
   #       return redirect(url_for('showall'))
   if request.method=='POST':
   		msg= msgs(username, "khachedu",request.form['chat'])
   		db.session.add(msg)
   		db.session.commit()
   		return render_template('showall.html',username=username,msgs = msgs.query.all())
   	
   return render_template('showall.html',username=username, msgs = msgs.query.all())

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
