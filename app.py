from flask import Flask,make_response
from flask_migrate import Migrate
from flask_restful import Api

from messages import message_chat

from models import db,Message

from models import db, Contact
from contacts import Contact_List, Contact_by_id


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chit-chat.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.json.compact = False

migrations =Migrate(app ,db)

db.init_app(app)

api=Api(app)


@app.route("/")
def hello():
    return "<h1>Hello chit-chat</h1>"

api.add_resource(Contact_List, '/contacts')
api.add_resource(Contact_by_id, '/contacts/<int:id>')

api.add_resource(message_chat, '/messages')


if __name__ == "__main__":

    app.run(port=5555)

