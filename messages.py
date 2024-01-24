
from models import Message
from flask_restful import Resource
from flask import make_response
from models import db

messages = []
class message_chat(Resource):
    def get(self):
            
