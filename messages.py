from flask_restful import Resource,Api
from models import Message

class Message_list (Resource):
    def get(self):
          response_dict_list = [n.to_dict() for n in Message_list.query.all()]

response = make_response(
            jsonify(response_dict_list),
            200,
        )
return response

