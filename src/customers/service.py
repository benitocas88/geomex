from flask.globals import current_app as app
from jwt import encode as jwt_encode, decode as jwt_decode
from datetime import datetime, timedelta
from customers.models import User
from customers.schemas import UserSchema

ACCESS_TOKEN_EXPIRES_IN_MINUTES = 15


class UserService:
    def signup(self, data) -> User:
        schema = UserSchema()
        user = schema.load(data)
        return user.save()

    @staticmethod
    def login(data):
        schema = UserSchema()
        auth = schema.load(data)
        user = User.query.filter(User.email == auth.email).first()
        if user and user.password == data['password']:
            return user
        return False

    @staticmethod
    def access_token(user: User) -> dict:
        user_dict = UserSchema(exclude=[User.password.key]).dump(user)
        exp = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN_MINUTES)
        user_dict.update(exp=exp.timestamp())
        jwt_secret_key = app.config.get('JWT_SECRET_KEY')
        return jwt_encode(user_dict, jwt_secret_key)

    @staticmethod
    def access_token_decode(access_token: str):
        jwt_secret_key = app.config.get('JWT_SECRET_KEY')
        return jwt_decode(access_token, jwt_secret_key)
