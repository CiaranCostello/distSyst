import requests
from flask import Flask, request
import os

file_folder = '~/Documents/fourth-year/distsyst/fileSystem/files/'

app = Flask(__name__)
app.config['FILE_FOLDER'] = file_folder

@app.route("/write", methods=['POST'])
def write_file():
	file = request.files['file']
	filepath = 'files/{filename}'.format(filename=file.filename)
	with open(filepath, 'wb') as open_file:
		open_file.write(file.read())
	return 'File stored successfully.'

@app.route('/read', methods=['GET'])
def read_file():
	
