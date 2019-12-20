import csv

inputfile = csv.reader(open('tweets.csv','r'))
outputfile = open('formatted_data.txt','w')

for row in inputfile:
    outputfile.write('<|startoftext|>' + row[0] + '<|endoftext|>')