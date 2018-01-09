The facebook API can be accessed using developers.facebook.com and signing up as a developer.
Refer to any online tutorial for the basics.
The Facebook API can be used to generate access tokens which are used in python programs to fetch data. 
####  The first program I will show here, can fetch upto 100 most recent posts on a page, using the page id as input.
   Check out the code [here](https://github.com/pooja7b/simplePythonPrograms/blob/master/showPagePosts.py)
#### The second program iterates over ALL posts on a page and determines whenever a new page occurs in the results.(pagination) 
   Check out the code [here](https://github.com/pooja7b/simplePythonPrograms/blob/master/fbPagination.py)
   
#### Create an app as a developer on Facebook to obtain appID. Write a Python program using this appID. Since you would be the ‘user’ of this app created by you, so you can grant all permissions to this app so that it collects most of your information. Specifically, your python program should output your own feed information and list down ‘all’ your friends. Do ‘all’ your friends get listed ? Give reasons for your answer.
 
#### The Answer:
After running [this code](https://github.com/pooja7b/Data-Science-And-ML/blob/master/find-fb-friends.py), it is observed that no output is returned when we try to retrieve all our friends on facebook.  On trying to query the Graph API explorer to see if we are able to do that, we find out the reason. Only those friends can be returned as output which have used the Graph API explorer app in the past. Analogously, since we are accessing the API through our app, which practically no one has used, we cannot see our friendlist using this python program.
