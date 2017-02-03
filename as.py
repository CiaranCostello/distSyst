#Authentication Server
#-maintains list of username password pairs
#-responds to (username, encrypted(password)) with token
#-stores symetric key for encryption of data between servers and clients
#-token = (ticket, sessionKey, serverID, timeoutPeriod)

from flask import Flask
app = Flask(__name__)

passwords = {'CiaranCostello': 'password1', 'JohnMurphy': 'password2'}
#key used to encrypt session key. Known by all servers
server_key = 'Mary had a little lamb'

@app.route("/sign_up", methods=[POST])
def sign_up():



#user sends (username, encrypted(password)) with token
@app.route("/sign_in")
def sign_in():


if __name__ == '__main__':
	app.run()