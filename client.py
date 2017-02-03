import argparse, requests

def send_file(url, port, filename):
	files = {'file': ('text.txt', open('text.txt', 'r'))}
	dest = 'http://{url}:{port}/write'.format(url=url, port=port)
	r = requests.post(dest, files=files)

def get_file(url, port, filename):
	fileparams = {'filename': filename}
	dest = 'http://{url}:{port}/read'.format(url=url, port=port)
	r = requests.get(dest, params=fileparams)
	print(r.status_code)
	if r.status_code == 200:
		with open(filename,'w+') as f:
			data = r.text
			f.seek(0)
			f.write(data)
			f.truncate()
			f.close()
		print('File successfully downloaded and saved to {}'.format(filename))

def clargs():
	parser = argparse.ArgumentParser(description='Client for a distributed file system')

	sub_parser = parser.add_subparsers(dest='cmd')
	sub_parser.required = True
	
	pull = sub_parser.add_parser('pull', help='pull a file from a dfs')
	push = sub_parser.add_parser('push', help='push a file to a dfs')

	#parser.add_argument('-h', '--host', required=True, help='hostname of fileserver')
	parser.add_argument('-u', '--url', required=True, help='url of the fileserver')
	parser.add_argument('-p', '--port', required=True, help='port on which the service is operating')
	parser.add_argument('-f', '--fileName', required=True, help='Filename for client to send')

	return parser.parse_args()

if __name__ == '__main__':
	args = clargs()
	if(args.cmd == 'push'):
		send_file(url=args.url, port=args.port, filename=args.fileName)
	if(args.cmd == 'pull'):
		get_file(url=args.url, port=args.port, filename=args.fileName)
