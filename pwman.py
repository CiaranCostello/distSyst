import crypt
import pwd
import redis

def login(username, password):
	username = input('Python login: ')
	cryptedpasswd = pwd.getpwnam(username)[1]
	if cryptedpasswd:
		if cryptedpasswd == 'x' or cryptedpasswd == '*':
			raise ValueError('no support for shadow passwords')
			cleartext = getpass.getpass()
			return compare_hash(crypt.crypt(cleartext, cryptedpasswd), cryptedpasswd)
		else:
			return True


hashed = crypt.crypt(plaintext)
	if not compare_hash(hashed, crypt.crypt(plaintext, hashed)):
		raise ValueError("hashed version doesn't validate against original")