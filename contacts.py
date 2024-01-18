from flask_restful import Resource
from models import Contacts


class Contact_List(Resource):

    def get(self, id):
        if id:
            contact = Contacts.query.filter_by(id = id).first()
            return contact
        else:
            contact = Contacts.query.all()

            return contact
        pass

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass