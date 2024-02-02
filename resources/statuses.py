from flask import make_response, jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models import db, Status


class Status_List(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('user_id', required=True, help="user_id is required")
    parser.add_argument('status_text', required=True, help="status_text is required")
    parser.add_argument('photo_url', required=False)

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
    @jwt_required()
    def post(self):
        data = Status_List.parser.parse_args()
        new_status = Status(**data)

        db.session.add(new_status)
        db.session.commit()

        status_dict = new_status.to_dict()

        response = make_response(
            jsonify(status_dict),
            201
        )

        return response
    


class Status_by_id(Resource):
    @jwt_required()
    def get(self, id):
        status = Status.query.filter_by(id = id).first()
        status_dict = status.to_dict()

        response = make_response(
            jsonify(status_dict),
            200,
        )
        return response

    @jwt_required()
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

    @jwt_required()
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