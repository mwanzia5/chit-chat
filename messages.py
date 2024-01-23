from flask_restful import Resource,jsonify,request
from models import Message
from flask import make_response
from models import db
class Message_List (Resource):
    def get(self,id):
            messages = Message.query.filter_by(id=id).first()

    if request.method == 'GET':
        message_dict = messages.to_dict()

        response = make_response(
            jsonify(message_dict),
            200
        )

        return response

    elif request.method == 'DELETE':
        db.session.delete(messages)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Review deleted."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response


      
