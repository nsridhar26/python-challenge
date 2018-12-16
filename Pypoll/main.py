import os
import csv
import pandas as pd
#relative path of CSV file
file_to_load = os.path.join(Pypoll\election_data.csv)
#open and read csv
with open(file_to_load, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# skip the header before the loop
Next(reader, None)
#print number of months in the data set
fname = input("file_to_load: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
            print("Total number of votes: ")
            print(num_lines)
#list of candidates who recieved votes
unq.column(2)