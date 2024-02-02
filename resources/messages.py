from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required
from models import db, Message



class Message_List(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sender_id', required=True, help="sender_id is required")
    parser.add_argument('receiver_id', required=True, help="receiver_id is required")
    parser.add_argument('message', required=True, help="message is required")
    parser.add_argument('media', required=False)


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
    
    @jwt_required()
    def post(self):
        data = Message_List.parser.parse_args()
        new_message = Message(**data)

        db.session.add(new_message)
        db.session.commit()

        message_dict = new_message.to_dict()

        response = make_response(
            jsonify(message_dict),
            201
        )

        return response
    
class Message_by_id(Resource):
    @jwt_required()
    def get(self, id):
        message = Message.query.filter_by(id = id).first()
        message_dict = message.to_dict()

        response = make_response(
            jsonify(message_dict),
            200,
        )
        return response
    
    @jwt_required()
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
    
    @jwt_required()
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
 

