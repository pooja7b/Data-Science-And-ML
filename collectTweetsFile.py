from twython import Twython

APP_KEY = "HJPwbpmvynoqrKs5F13KC3HGE"
APP_SECRET = "G5VTpecAmsfDp9vlmoXIDjjqW7T81MIjSF0yz9MdjqUSt6VnuS"
OAUTH_TOKEN = "713407156700073984-Ub9FiuF02oBssBLHVhvaq4HLYUHBka6"
OAUTH_TOKEN_SECRET = "epY5EQcpmYQ8JAyt4lVu0o80sxzuKbiwv8kx0nceDUhow" 

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) 

f = open('collected_data.txt','w')

username=raw_input("Enter username: ")
user_timeline  = twitter.get_user_timeline(screen_name=username, count = 1000)
for tweet in user_timeline:
	print >> f,tweet
	f.write("\n")
