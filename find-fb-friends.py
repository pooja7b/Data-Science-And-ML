import requests
import json

token = 'your-access-token-goes-here'
id = *****  # your profile id goes here
print "Friend Details"
url = 'https://graph.facebook.com/'+str(id)+'/friendlists?fields=name&limit(100)&access_token='+token
data = requests.get(url)
response = json.loads(data.text)
for friend in response['data']:
	print friend['id']
	print friend['name']
	print "\n"
