#ATUL_KONAJE 5198 
#CSE6331 ATUL.KONAJE@mavs.uta.edu
import pymongo
from pymongo import MongoClient
import hashlib
from bson.binary import Binary
from datetime import datetime
import base64
#Get MongoDB instance
mClient =MongoClient()
#Create/Get existing DB
mDB=mClient.Photobook_db

def enc_pwd(passwd):
    return hashlib.md5(passwd).hexdigest()

def create_user(uname,passwd,Gender):
    user_coll=mDB.C_userdata
    password=enc_pwd(passwd)
    user_exists=user_coll.find_one({"username":uname})
    if(user_exists):
        return "User with this name already exists"
    else:
        user_coll.insert_one({"username":uname,"pwd":password})
        return "User account created"    
def authenticate_user(uname,passwd):
    user_coll= mDB.C_userdata
    password = enc_pwd(passwd)
    print password
    for i in user_coll.find({"username":uname}):
        if(i['pwd']==password):
            return True
        else:
            return False

#http://stackoverflow.com/questions/11915770/saving-picture-to-mongodb
def insertImage(image_data,username,img_UUID,comments,img_name):
    encoded_string = base64.b64encode(image_data)
    try:
	img_ins=mDB.C_images.insert_one({"owner":username,"image":encoded_string,"image_UUID": str(img_UUID),"time":datetime.now(),"comments":comments,"imagename":img_name})
    except Exception:
        print Exception
        return False
    if (img_ins):
        return True

def retrieveUPimage(uuid,uname):
    rec = mDB.C_images.find_one({"image_UUID":uuid,"owner":uname})
    decode=rec["image"].decode()
    img_tag = format(decode)
    return img_tag
    
def allmyimages(uname):
    records= mDB.C_images.find({"owner":uname})
    return records

def allimages():
    records=mDB.C_images.find()
    return records

def saveComment(uname,comment,uid):
    print uid
    rec=mDB.C_images.find_one({"image_UUID":uid})
    cur_time=str(datetime.now()).replace("-","").replace(":","").replace(".","")
    rec['comments'][cur_time]={"user":uname,"user_comment":comment}
    mDB.C_images.save(rec)
    return True

def retrieveComments(uuid):
    rec=mDB.C_images.find_one({"image_UUID":uuid})
    comm={}
    comm["comment"]=[]
    comm["uuid"]=uuid
    c_keys=rec["comments"].keys()
    c_keys.sort()
    for tim in c_keys:
        comm["comment"].append(rec["comments"][tim])
    print comm
    for i in  comm:
        print i
    return comm

def delete_image(uuid):
    mDB.C_images.delete_one({"image_UUID":uuid})
    return "Deleted Successfuly"

