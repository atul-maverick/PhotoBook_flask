from flask import Flask, send_from_directory, Blueprint, request
from flask_restful import Resource, Api
from flask_jwt.flask_jwt import JWT, jwt_required
from flask import curent_app as app
import pdb
import py_mongo
from flaskApp import app
passwd=Blueprint('password', __name__)
api=Api(passwd)


@app.route('/pwd/checkpasswd',methods=['POST'])
@jwt_required()
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


