#Authentication Server
#-maintains list of username password pairs
#-responds to (username, encrypted(password)) with token
#-stores symetric key for encryption of data between servers and clients
#-token = (ticket, sessionKey, serverID, timeoutPeriod)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "hello world"



if __name__ == '__main__':
	app.run()