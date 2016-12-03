#!/usr/bin/env python
from flask import Flask, request, flash, url_for, redirect, render_template,jsonify
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

@app.route('/')
def welcome():
   return ''' <h1>hello kartikey</h1>'''

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
        print msgs.query.all()
        return render_template('showall.html',username=username,msgs = msgs.query.all())
        #return jsonify(msgs.query.all());

    
    return render_template('showall.html',username=username, msgs = msgs.query.all())
    #return jsonify(samp=samp);

@app.route('/getchats', methods = ['GET', 'POST'])
def getchat():
    samp=[]
    all_msgs = msgs.query.all()
    for msg in all_msgs:
        dict={"to" :msg.msg_to,"from":msg.msg_from,"message":msg.msg}
        samp.append(dict)
    for s in samp:
        print s
    #return render_template('showall.html',username=username, msgs = msgs.query.all())
    return jsonify(samp=samp);

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
