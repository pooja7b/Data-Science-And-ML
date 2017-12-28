import sys
mylist=map(float,raw_input('enter list of numbers:').split(","));
for i in mylist:
	try:
	    print (2/i);
	except ZeroDivisionError:
	    print ("Cannot divide by zero");
