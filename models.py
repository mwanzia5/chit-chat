from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-message.user',)
    
    id = db.Column(db.Integer,primary_key = True)
    first_name =db.Column(db.String,nullable = False)
    last_name  = db.Column (db.String,nullable = False)
    phone_number = db.Column(db.String,nullable = False ,unique=True)
    password = db.Column (db.VARCHAR ,nullable = False)
    profile_photo = db.Column (db.VARCHAR ,nullable = True)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())

    messages = db.relationship('Message', backref = 'user')
    
    def __repr__(self):
        return {"id": self.id, 
                "first_name": self.first_name, 
                "last_name": self.last_name,
                "phone_number": self.phone_number,
                "profile_photo": self.profile_photo
                }
    
    def check_password(self,plain_password):
        return check_password_hash(self.password,plain_password)
    
    def to_json(self):
        return {"id": self.id, 
                "first_name": self.first_name, 
                "last_name": self.last_name,
                "phone_number": self.phone_number,
                "profile_photo": self.profile_photo
                }



class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    serialize_rules = ('-user', '-contact',)

    id = db.Column(db.Integer,primary_key = True)
    contact_id= db.Column(db.Integer,db.ForeignKey('contacts.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    message = db.Column(db.VARCHAR,nullable = True)
    sent_at = db.Column(db.TIMESTAMP,server_default=db.func.now())
    media = db.Column(db.VARCHAR,nullable=True)

    def __repr__(self):
        return {"id": self.id, 
                "contact_id": self.contact_id, 
                "user_id": self.user_id,
                "message": self.message,
                "media": self.media,
                "sent_at": self.sent_at
                }


class Contact(db.Model, SerializerMixin):
    __tablename__ = 'contacts'

    serialize_rules = ('-messages.contact','-messages.user')

    id = db.Column(db.Integer,primary_key = True)
    first_name =db.Column(db.String,nullable = False)
    last_name  = db.Column (db.String,nullable = False)
    phone_number = db.Column(db.String,nullable = False ,unique=True)
    about=db.Column(db.VARCHAR,nullable=True)
    profile_photo = db.Column (db.VARCHAR ,nullable = True)
    previous_chat=db.Column(db.VARCHAR,nullable = True)
    last_seen=db.Column(db.TIMESTAMP,server_default=db.func.now())

    messages = db.relationship('Message', backref = 'contact')

    def __repr__(self):
        return {"id": self.id, 
                "first_name": self.first_name, 
                "last_name": self.last_name,
                "phone_number": self.phone_number,
                "about": self.about,
                "profile_photo": self.profile_photo,
                "previous_chat": self.previous_chat,
                "last_seen": self.last_seen
                }


