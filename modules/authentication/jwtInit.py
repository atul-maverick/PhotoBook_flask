#from flask_jwt.flask_jwt import JWT, jwt_required
import py_mongo



class User(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

def authenticate(uname, password):
    print(uname, password)
    print(py_mongo.authenticate_user(uname, password))
    if py_mongo.authenticate_user(uname, password):
        return User(username=uname)



def load_user(payload):

    return User(username=payload['identity'])

