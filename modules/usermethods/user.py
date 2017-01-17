from flask import Flask, send_from_directory, Blueprint, request
from flask_restful import Resource, Api
import pdb
import py_mongo
import uuid
user=Blueprint('user', __name__)
api=Api(user)
class User(Resource):
	def post(self):
		uname_param1= request.json["username"]
		pwd= request.json["password"]
		gender=request.json["gender"]
		return py_mongo.create_user(uname_param1,pwd,gender)
		
api.add_resource(User,'/signup','/')