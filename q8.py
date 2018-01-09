from __main__ import *
import csv

with open('test.csv') as f:
     a = [{k: str(v) for k, v in row.items()}
          for row in csv.DictReader(f, skipinitialspace=True)]
o = open('output.json','w')
print >>o,a


