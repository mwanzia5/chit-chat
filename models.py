from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    first_name =db.Column(db.String,nullable = False)
    last_name  = db.Column (db.String,nullable = False)
    phone_number = db.Column(db.String,nullable = False ,unique=True)
    password = db.Column (db.VARCHAR ,nullable = False)
    profile_photo = db.Column (db.VARCHAR ,nullable = True)
    created_at = db.column (db.TIMESTAMP)

class Messages (db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer,primary_key = True)
    contact_id= db.Column(db.VARCHAR,nullable=True)
    user_id = db.Column(db.VARCHAR,nullable = True)
    message = db.Column(db.VARCHAR,nullable = True)
    sent_at = db.Column(db.TIMESTAMP)
    media = db.Column(db.VARCHAR,nullable=True)


class Contacts(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer,primary_key = True)
    first_name =db.Column(db.String,nullable = False)
    last_name  = db.Column (db.String,nullable = False)
    phone_number = db.Column(db.String,nullable = False ,unique=True)
    about=db.Column(db.VARCHAR,nullable=True)
    profile_photo = db.Column (db.VARCHAR ,nullable = True)
    previous_chat=db.Column(db.VARCHAR,nullable = True)
    last_seen=db.Column(db.TIMESTAMP)


