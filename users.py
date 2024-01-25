from flask_restful import Api, Resource, request
from app import bcrypt
from flask_Bcrypt import generate_password_hash
from flask_jwt_extended import create_access_token
from models import db, User

class User_Signup(Resource):
    def post(self):
        
        # Extract user information from the request
        new_user = User(
            first_name = request.form.get("first_name"),
            last_name = request.form.get("last_name"),
            phone_number = request.form.get("phone_number"),
            password = request.form.get("password"),
            profile_photo = request.form.get("profile_photo"),
            )
        
        # Validate if phone and password are provided
        # if not new_user.phone_number or not new_user.password:
        #     return {'message': 'Both phone and password are required'}, 400

        # Check if the phone number is already registered
        if User.query.filter_by(phone_number = new_user.phone_number).first():
            return {'message': 'Phone number already registered'}, 400

        # Add the new user to the database
        new_user = User(phone_number=new_user.phone_number, password=generate_password_hash(new_user.password).decode('utf-8'))
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201


class User_Login(Resource):
    def post(self):
        data = request.get_json()

        # Extract user information from the request
        phone_number = data.get('phone number')
        password = data.get('password')

        # Find the user with the provided phone number
        user = User.query.filter_by(phone_number=phone_number).first()

        if user:
            # check if provided password is correct
            is_password_correct = user.check_password(password)

            if is_password_correct:
                # Generate token and return user dict
                user_json = user.to_json()
                access_token = create_access_token(identity=user_json['id'])
                return {'message': 'Login successful', 'access_token': access_token}, 200
            else:
                return {'message': 'Invalid phone number or password'}, 401
        else:
            return {'message': 'User not found'}, 404
