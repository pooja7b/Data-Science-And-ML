import csv
import q8
fout = open("output.csv", "w")
for value in q8.a:
	value['marks']=67
	print >>fout, value['name'],",",value['rollno'],",",value['marks']
