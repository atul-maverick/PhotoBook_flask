from flask import Flask, send_from_directory, Blueprint, request,_request_ctx_stack as requestack
from flask_restful import Resource, Api
import py_mongo
import uuid
import pdb
from flask_jwt.flask_jwt import jwt_required
image=Blueprint('image', __name__)
import json
api=Api(image)

class Image(Resource):
    @jwt_required()
    def post(self):
        #pdb.set_trace()
        img_data = request.files['file'].read()
        fname = request.files['file'].filename
        uname = request.values['username']
        image_UUID = uuid.uuid4()
        comments = {}
        m_response = py_mongo.insertImage(img_data, uname, image_UUID, comments, fname)
        response = {}

        if (m_response):
            response["img"] = {"uuid": str(image_UUID), "username": uname}
            response["message"] = "Successfuly uploaded"
            return json.dumps(response)
        else:
            return "Failed to upload image"

    @jwt_required()
    def get(self,imageid):

        currentuser=requestack.top.current_identity.username
        if imageid=="allimages":
            return getAllmyImages(currentuser)
        else:
            uuid_param1 = imageid
            uname_param2 = currentuser
            image_tag = py_mongo.retrieveUPimage(uuid_param1, uname_param2)
            print "retrieving"
            return image_tag

def getAllmyImages(currentuser):
    all_records = py_mongo.allmyimages(currentuser)
    response={}
    #pdb.set_trace()
    for record in all_records:
        response[str(record["image_UUID"])] = record["image"]
    return json.dumps(response)


api.add_resource(Image,'/','/<imageid>')