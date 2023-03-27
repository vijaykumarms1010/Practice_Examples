from flask import Flask,request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
api = Api(app)

class Employee(Resource):
    def get(self,empno,name,deptId):
        if empno==0:
            abort(404,message="Employee Id not found")

