from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime 
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class Messageboard(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.Text())
    timestamp = db.Column(db.DateTime)
    def __init__(self, messages,timestamp):
       self.messages = messages
       self.timestamp =timestamp
 
db.create_all()
db.session.commit()

@app.route("/")
def home():
    new_message = request.args.get('msg')
    if new_message:
        timestamp = datetime.datetime.now()
        data = Messageboard(new_message,timestamp)
        db.session.add(data)
        db.session.commit()
    feedbacks = Messageboard.query.all()
    return render_template('home.html', results=feedbacks)