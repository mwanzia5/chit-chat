
from models import Message
from flask_restful import Resource,jsonify
from flask import make_response
from models import db
from seed import messages

class message_chat(Resource):
    def get(self):
        message_chat = []
        for message in Message.query.all():
            message_dict = messages.append(message_dict)

        response = make_response(
           jsonify(messages),
             200
       )
        return response

            
