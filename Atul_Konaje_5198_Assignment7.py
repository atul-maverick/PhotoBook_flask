#Atul Konaje (Atul.Konaje@mavs.uta.edu)
#UTA ID 1001145198
#Course CSE6331 (2155-CSE-6331-004-ADV-TOPICS-IN-DATABASE-SYSTEMS--2015-Summer)
# import the Bottle framework
from bottle import Bottle, static_file
from bottle import route, template, request, error, debug,run
import json
import matplotlib
matplotlib.use('Agg')
from scipy.cluster.vq import *
import pylab
pylab.close()
import py_mongo
import uuid
#To send the html page on browser request
@route('/',method ="GET")
def welcome():
    output = static_file('login_page.html',root="views/")
    return output


@route('/scripts/app.js',method ="GET")
def welcome():

    output = static_file('app.js',root="scripts/")
    return output

@route('/modules/<path1>/<jsfile>', method="GET")
def peer(path1,jsfile):
	output =static_file(jsfile,root="modules/"+path1+"/")
	return output

@route('/modules/<path1>/<path2>/<resourcefile>',method="GET")
def send(path1,path2,resourcefile):
    output =static_file(resourcefile,root="modules/"+path1+"/"+path2+"/")
    return output


#i@route('/modules/authentication/views/login.html',method="GET")
#def send():
#    output =static_file('login.html',root="modules/authentication/views/")
#    return output

#@route('/modules/home/views/home.html',method="GET")
#def send():
#    output =static_file('home.html',root="modules/home/views/")
#    return output

#During login
@route('/checkpasswd',method='POST')
def check_passwd():
    request_json=request.json
    #import pdb
    #pdb.set_trace()
    uname= request_json["uname"]
    pwd= request_json["passwd"]
    #Check if username and password are legitimate
    if(py_mongo.authenticate_user(uname,pwd)):
        response="True"
    else:
        response="False"
    return response
#For picture upload
@route('/uploadpics',method = 'POST')
def upload_pics():
    #print"In upload function"
    #print dir(request)
    #import pdb
    #pdb.set_trace()
    img_data=request.files['file'].file.read()
    fname=request.files['file'].filename
    uname=request.params['username']
    image_UUID= uuid.uuid4()
    comments={}
    m_response=py_mongo.insertImage(img_data,uname,image_UUID,comments,fname)
    response={}
   
    if(m_response):
        response["img"]={"uuid":str(image_UUID),"username":uname}
        response["message"]= "Successfuly uploaded"
        return json.dumps(response)
    else:
        return "Failed to upload image"

#To get uploaded picture    
@route('/getupimage',method = 'POST')
def getUimage():
    uuid_param1=request.json["uuid"]
    uname_param2=request.json["username"]
    image_tag=py_mongo.retrieveUPimage(uuid_param1,uname_param2)
    print "retrieving"
    return image_tag
#To get all current users picture
@route('/getAllMyImage',method = 'POST')
def getAllmyImages():
     uname_param2=request.json["username"]
     print uname_param2
     response={}
     #response["Images"]={}
     all_records=py_mongo.allmyimages(uname_param2)
     for record in all_records:
       response[str(record["image_UUID"])] = record["image"]
     #return response
     #for i in range(1,4):
         #response.append(i)
     return json.dumps(response)

#To get everyones picture
@route('/getAllImages',method= 'POST')
def getAllImages():
    response={}
    all_records=py_mongo.allimages()
    for record in all_records:
        response[str(record["image_UUID"])] = record["image"]
    return json.dumps(response)

@route('/postcomment',method='POST')
def postcomment():
    #pdb.set_trace()
    comment_param2=request.json["comment"]
    uname_param1= request.json["username"]
    uuid_param3=request.json["uuid_data"]
    py_mongo.saveComment(uname_param1,comment_param2,uuid_param3)
    py_mongo.retrieveComments(uuid_param3)

#To get all comments of a picture
@route('/getComments',method='POST')
def getComments():
    uuid_param1=request.json["uuid_data"]
    records=py_mongo.retrieveComments(uuid_param1)
    return json.dumps(records)

#To delete image
@route('/deleteImg',method='POST')
def delImage():
    uuid_param1=request.json["uuid_data"]
    resp=py_mongo.delete_image(uuid_param1)
    return resp

#Creating new user
@route('/signup',method='POST')
def create_user():
    uname_param1= request.json["username"]
    pwd= request.json["password"]
    gender=request.json["gender"]
    return py_mongo.create_user(uname_param1,pwd,gender)


run(host='0.0.0.0', port=3000, debug=True)

