from flask import make_response, jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models import db, Status

class Status_List(Resource):
    @jwt_required()
    def get(self):
        status_list = []
        for status in Status.query.all():
            status_dict = status.to_dict()
            status_list.append(status_dict)

        response = make_response(
            jsonify(status_list),
            200,
        )
        return response
    
    def post(self):
        new_status = Status(
            status_text = request.get_json().get("status_text"),
            photo_url = request.get_json().get("photo_url"),
            user_id = request.get_json().get("user_id"),
            )
        db.session.add(new_status)
        db.session.commit()

        status_dict = new_status.to_dict()

        response = make_response(
            jsonify(status_dict),
            201
        )

        return response
    
class Status_by_id(Resource):

    def get(self, id):
        status = Status.query.filter_by(id = id).first()
        status_dict = status.to_dict()

        response = make_response(
            jsonify(status_dict),
            200,
        )
        return response


    def patch(self,id):
        status = Status.query.filter_by(id = id).first()
        for attr in request.get_json():
            setattr(status, attr, request.get_json().get(attr))

        db.session.add(status)
        db.session.commit()

        status_dict = status.to_dict()

        response = make_response(
            jsonify(status_dict),
            201
        )

        return response


    def delete(self,id):
        status = Status.query.filter_by(id = id).first()
        db.session.delete(status)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Contact deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response