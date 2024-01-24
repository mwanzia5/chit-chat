
from models import Message
from flask_restful import Resource
from flask import make_response,jsonify 
from models import db
from seed import messages

class message_chat(Resource):

 def get(self):
    message_chat = []
    for message in Message.query.all():
        message_dict =  messages.append(message_dict)

    response = make_response(
        jsonify(message_chat),
        200
    )

    return response


            