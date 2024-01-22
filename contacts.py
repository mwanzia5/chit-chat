from flask import make_response, jsonify, request
from flask_restful import Resource, fields, marshal_with, reqparse
from models import db,Contact


class Contact_List(Resource):

    def get(self):
        contact_list = []
        for contact in Contact.query.all():
            contact_dict = contact.to_dict()
            contact_list.append(contact_dict)

        response = make_response(
            jsonify(contact_list),
            200,
        )
        return response
    
    def post(self):
        new_contact = Contact(
            first_name = request.form.get("first_name"),
            last_name = request.form.get("last_name"),
            phone_number = request.form.get("phone_number"),
            about = request.form.get("about"),
            profile_photo = request.form.get("profile_photo"),
            previous_chat = request.form.get("previous_chat"),
            )
        db.session.add(new_contact)
        db.session.commit()

        contact_dict = new_contact.to_dict()

        response = make_response(
            jsonify(contact_dict),
            201
        )

        return response
    
class Contact_by_id(Resource):

    def get(self, id):
        contact = Contact.query.filter_by(id = id).first()
        contact_dict = contact.to_dict()

        response = make_response(
            jsonify(contact_dict),
            200,
        )
        return response


    def patch(self,id):
        contact = Contact.query.filter_by(id = id).first()
        for attr in request.form:
            setattr(contact, attr, request.form.get(attr))

        db.session.add(contact)
        db.session.commit()

        contact_dict = contact.to_dict()

        response = make_response(
            jsonify(contact_dict),
            201
        )

        return response


    def delete(self,id):
        contact = Contact.query.filter_by(id = id).first()
        db.session.delete(contact)
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

            # if id:
        #     contact = Contacts.query.filter_by(id = id).first()
        #     return contact
        # else:
        #     contact = Contacts.query.all()

        #     return contact
