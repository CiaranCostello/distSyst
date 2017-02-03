# Node containing files
# Provides read and write methods and registers with a master server

import requests
from flask import Flask, request, send_file
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
	try:
		filename = request.args.get('filename')
		filepath = 'files/{filename}'.format(filename=filename)
		return send_file(filepath, attachment_filename=filename)
	except Exception as e:
		return str(e)
