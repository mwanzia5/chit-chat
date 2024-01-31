
from models import Message
from flask_restful import Resource
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required
from models import db


class message_chat(Resource):
 @jwt_required()
 def get(self):
    message_chat = []
    for message in Message.query.all():
        message_dict =  message.to_dict()
        message_chat.append(message_dict)

    response = make_response(
        jsonify(message_chat),
        200
    )

    return response
 
 def post(self):
        new_message = Message(
            contact_id = request.get_json().get("contact_id"),
            user_id = request.get_json().get("user_id"),
            message = request.get_json().get("message"),
            media = request.get_json().get("media")
            )
        db.session.add(new_message)
        db.session.commit()

        message_dict = new_message.to_dict()

        response = make_response(
            jsonify(message_dict),
            201
        )

        return response
    

class messages_by_id(Resource):

 def patch(self,id):
        message = Message.query.filter_by(id = id).first()
        for attr in request.get_json():
            setattr(message, attr, request.get_json().get(attr))

        db.session.add(message)
        db.session.commit()

        message_dict = message.to_dict()

        response = make_response(
            jsonify(message_dict),
            201
        )

        return response
    
 def delete(self,id):
        message = Message.query.filter_by(id = id).first()
        db.session.delete(message)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Message deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )


        return response
