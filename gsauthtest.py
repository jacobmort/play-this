import urllib
import md5
import simplejson

def gsAuth():
	url = 'http://1.apishark.com/p:y3p001/genGSAuth/'
	username = 'ubien'
	pw = 'kflip402'
	token = md5.new(username + md5.new(pw).hexdigest()).hexdigest()
	params = urllib.urlencode({'username': username, 'token': token})
	f = urllib.urlopen(url, params)
	#auth_resp = f.read()
	result = simplejson.load(f)
	token = -1
	if result['Success'] == True:
		token = result['Result']
	return token


