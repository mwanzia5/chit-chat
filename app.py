from flask import Flask
from flask_migrate import Migrate
from messages import Message_list
from flask_restful import Api
from models import db
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


api.add_resource(Message_list, '/messages')

if __name__ == "__main__":
    app.run(debug=True)
