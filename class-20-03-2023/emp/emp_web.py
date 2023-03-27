from flask import Flask,request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
api = Api(app)


class Employee(Resource):
    def get(selfself,emp_id):
        if emp_id==0:
            abort(404,message="Invalid employee id")
        return {"msg":"get employee Id"}
    def post(selfself,emp):