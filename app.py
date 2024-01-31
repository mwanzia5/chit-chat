
from flask import Flask,make_response ,jsonify
from flask_migrate import Migrate
from flask_restful import Api,Resource ,request, reqparse
from flask_cors import CORS
from flask_bcrypt import Bcrypt , generate_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from datetime import timedelta
from messages import message_chat,messages_by_id
from models import db,Message,Contact ,User
from contacts import Contact_List, Contact_by_id
from statuses import Status_List, Status_by_id


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chit-chat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.json.compact = False

migrations =Migrate(app ,db)

db.init_app(app)

api=Api(app)
CORS(app)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)


@app.route("/")
def hello():
    return "<h1>Hello chit-chat</h1>"


class User_Signup(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True, help="Firstname is required")
    parser.add_argument('last_name', required=True, help="Last_name is required")
    parser.add_argument('phone_number', required=True, help="Phone number is required")
    parser.add_argument('password', required=True, help="Password is required")
    parser.add_argument('profile_photo', required=False)

    def post(self):
        
        # Extract user information from the request
        data = User_Signup.parser.parse_args()
        new_user = User(**data)
        print(new_user.first_name)
        print(new_user.last_name)
        
        # Validate if phone and password are provided
        if not new_user.phone_number or not new_user.password:
            return {'message': 'Both phone and password are required'}, 400

        # Check if the phone number is already registered
        if User.query.filter_by(phone_number = new_user.phone_number).first():
            return {'message': 'Phone number already registered'}, 400

        new_user.password = generate_password_hash(new_user.password).decode('utf-8') 

        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201


class User_Login(Resource):
        parser = reqparse.RequestParser()
        parser.add_argument('phone_number', required=True, help="Email address is required")
        parser.add_argument('password', required=True, help="Password is required")
        
        def post(self):

            data = User_Login.parser.parse_args()

            # Extract user information from the request
            # phone_number = request.form.get('phone_number')
            # password = request.form.get('password')
            # print(phone_number)
            # print(password)

            # Find the user with the provided phone number
            user = User.query.filter_by(phone_number= data['phone_number']).first()

            if user:
                # check if provided password is correct
                is_password_correct = user.check_password(data['password'])

                if is_password_correct:
                    # Generate token and return user dict
                    user_json = user.to_json()
                    access_token = create_access_token(identity=user_json['id'])
                    refresh_token = create_refresh_token(identity=user_json['id'])
                    return {"message": "Login successful",
                            "status": "success",
                            "access_token": access_token,
                            "refresh_token": refresh_token,
                            "user": user_json,
                            }, 200
                else:
                    return {'message': 'Invalid phone number or password'}, 401
            else:
                return {'message': 'User not found'}, 404
            

class RefreshAccess(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()

        access_token = create_access_token(identity=identity)

        return jsonify(access_token = access_token)



api.add_resource(Contact_List, '/contacts')
api.add_resource(Contact_by_id, '/contacts/<int:id>')

api.add_resource(message_chat, '/messages')
api.add_resource(messages_by_id, '/messages/<int:id>')

api.add_resource(User_Signup, '/signup')
api.add_resource(User_Login, '/login')

api.add_resource(Status_List, '/statuses')
api.add_resource(Status_by_id, '/statuses/<int:id>')

api.add_resource(RefreshAccess, '/refreshaccess')



if __name__ == "__main__":
    app.run(port=5555,debug=True)
