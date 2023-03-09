from flask_restful import Resource
from flask.globals import request


class Customer(Resource):
    def post(self):
        email = request.form.get("email")
        password = request.form.get("password")
        print(email, password)
        return {}
