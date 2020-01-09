import csv 
import itertools 
import sys 

argumentList = sys.argv


filename = argumentList[1] 
  
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
    for row in csvreader: 
        rows.append(row) 
#getting characters
for i in range(len(rows)):
    rows[i]= [x for x in rows[i] if x]

#making permutation of all arrays  
for n in itertools.product(*rows):
   print(''.join(n))
