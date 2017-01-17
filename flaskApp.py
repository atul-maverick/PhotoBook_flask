from flask import Flask, send_from_directory, Blueprint
from flask_restful import Resource, Api
from modules.authentication.loginpage import loginpage
from modules.resourcefiles.scripts import files,jsfiles
from modules.usermethods.user import user
from modules.usermethods.passwd import passwd
app = Flask(__name__,static_folder="templates/views")



app.register_blueprint(loginpage,url_prefix="/");
app.register_blueprint(files, url_prefix="/scripts")
app.register_blueprint(jsfiles, url_prefix= "/modules")
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(passwd, url_prefix="/user/pwd")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)
