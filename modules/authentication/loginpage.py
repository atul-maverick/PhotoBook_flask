from flask import Flask, Blueprint
loginpage = Blueprint('loginpage', __name__,static_folder="../../templates/views")
@loginpage.route('/')
def get():
	print "Got it"
	return loginpage.send_static_file('login_page.html')