from flask import make_response
from flask_restful import Resource,jsonify
from models import Message

class MessageList (Resource):
    def get(self,id):
                  
       message_dict= Message.query.filter_by(id=id).first().to_dict()

       message= make_response(
            jsonify(message_dict),
            200,
        )

       return message



