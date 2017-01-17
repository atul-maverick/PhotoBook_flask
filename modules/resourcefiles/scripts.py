from flask import Flask, Blueprint, send_from_directory
files = Blueprint('files', __name__)
@files.route('/<rfile>')
def get(rfile):
	return send_from_directory('scripts', rfile)

jsfiles = Blueprint('jsfiles', __name__)
@jsfiles.route('/<path1>/<rfile>')
def jsget(path1,rfile):
	return send_from_directory('modules/'+path1, rfile)
  
@jsfiles.route('/<path1>/<path2>/<rfile>')
def jsget1(path1,path2,rfile):
	return send_from_directory('modules/'+path1+"/"+path2, rfile)    