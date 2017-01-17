from flask import Flask, send_from_directory, Blueprint, request
from flask_restful import Resource, Api
import pdb 
import py_mongo

passwd=Blueprint('password', __name__)
api=Api(passwd)

# class Password(Resource):
	# def put(self):
	
		
		
# api.add_resource(Password,'/')

@passwd.route('/checkpasswd',methods=['POST','GET'])
def check_passwd():
    request_json=request.json
    uname= request_json["uname"]
    pwd= request_json["passwd"]
    #Check if username and password are legitimate
    if(py_mongo.authenticate_user(uname,pwd)):
        response="True"
    else:
        response="False"
    return response