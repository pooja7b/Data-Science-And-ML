import sys
str1="".join(sys.argv[1:2])
#print str1
str2="".join(sys.argv[2:3])
#print str2
if str1.find(str2)!= -1:
  print ("Match")
else :
  print ("No Match")

