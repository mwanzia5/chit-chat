from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-password',)
    
    id = db.Column(db.Integer,primary_key = True)
    first_name =db.Column(db.String,nullable = False)
    last_name  = db.Column (db.String,nullable = False)
    phone_number = db.Column(db.String,nullable = False ,unique=True)
    password = db.Column (db.VARCHAR ,nullable = False)
    profile_photo = db.Column (db.VARCHAR ,nullable = True)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())

    messages_sent = db.relationship('Message', backref = 'sender', foreign_keys = 'Message.sender_id')
    messages_received = db.relationship('Message', backref = 'receiver', foreign_keys = 'Message.receiver_id')
    statuses = db.relationship('Status', backref = 'user')
    
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

    serialize_rules = ('-sender', '-receiver',)

    id = db.Column(db.Integer,primary_key = True)
    message = db.Column(db.VARCHAR,nullable = True)
    sent_at = db.Column(db.TIMESTAMP,server_default=db.func.now())
    media = db.Column(db.VARCHAR,nullable=True)
    
    sender_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    receiver_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return {"id": self.id, 
                "contact_id": self.contact_id, 
                "user_id": self.user_id,
                "message": self.message,
                "media": self.media,
                "sent_at": self.sent_at
                }


    
class Status(db.Model, SerializerMixin):
    __tablename__ = 'statuses'

    serialize_rules = ('-user',)
# 
    id = db.Column(db.Integer,primary_key = True)
    status_text = db.Column(db.String,nullable = False)
    sent_at = db.Column(db.TIMESTAMP,server_default=db.func.now())
    photo_url  = db.Column (db.VARCHAR ,nullable = True)

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return {"id": self.id, 
                "status_text": self.status_text, 
                "sent_at": self.sent_at,
                "photo_url": self.photo_url,
                "user_id": self.user_id,
                }