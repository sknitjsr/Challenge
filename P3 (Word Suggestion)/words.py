import csv 
import sys 
from difflib import get_close_matches 
argumentList = sys.argv


filename = sys.argv[1]
  
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
    for row in csvreader: 
        rows.append(row) 
        #appending data to row 2-d array
        
patterns = []
for x in rows :
    patterns.append(x[0])
    
    
word = sys.argv[2]

res = get_close_matches(word, patterns,5,0)
        
  
print(res)
 
  
