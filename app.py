from flask import Flask, send_from_directory, Blueprint, request
from flask_restful import Resource, Api
from modules.authentication.loginpage import loginpage
# from modules.authentication.passwd import passwd
from modules.resourcefiles.scripts import files, jsfiles
from modules.usermethods.user import user
from flask_jwt.flask_jwt import JWT, jwt_required
import py_mongo
from modules.usermethods.images import image
from modules.authentication.jwtInit import authenticate, load_user

app = Flask(__name__, static_folder="templates/views")

jwt = JWT()

app.register_blueprint(loginpage, url_prefix="/");
app.register_blueprint(files, url_prefix="/scripts")
app.register_blueprint(jsfiles, url_prefix="/modules")
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(image, url_prefix="/image")

app.config['SECRET_KEY'] = 'super-secret'
app.debug = True

jwt.authentication_handler(authenticate)

jwt.identity_handler(load_user)


jwt.init_app(app)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=3000)
