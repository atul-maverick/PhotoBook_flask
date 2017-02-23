from flask import Flask, Blueprint, current_app

loginpage = Blueprint('loginpage', __name__, static_folder="../../templates/views")

@loginpage.route('/')
def get():
    return loginpage.send_static_file('login_page.html')

#
# jwt = JWT()
#
#
# class User(object):
#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             setattr(self, k, v)
#
#
# @jwt.authentication_handler
# def authenticate(uname, password):
#     print(uname, password)
#     if py_mongo.authenticate_user(uname, password):
#         return User(id=1, username=uname)
#
#
# @jwt.identity_handler
# def load_user(payload):
#     print(payload)
#     return User(id=1, username='test')
#
#
# jwt.init_app(app)
