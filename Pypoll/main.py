import os
import csv

#relative path of CSV file
election_dt = os.path.join('Pypoll','election_data.csv')

# Declared/set variable and set to 0 or list/dictionary
total_votes = 0
candidates = []
percentage_votes = []
number_votes = []
win = []

#open and read csv
with open(election_dt, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# skip the header before the loop
next(csvreader, None)
#print number of rows in the data set
fname = input("election_dt: ")
num_lines = 0
with open(fname, 'r') as f:
    for row in f:
        total_votes += 1
        print("Total number of votes: ")
        print(num_lines)
#list of candidates who recieved votes
        if row["Candidate"] not in candidates:
            
            candidates.append(row["Candidate"])

            number_votes[row["Candidate"]] = 1
        else:
            number_votes[row["Candidate"]] = number_votes[row["Candidate"]] + 1
# identify total votes for every candidate and divide by total votes
percentage_votes = number_votes/total_votes
#find the winner 
win = max(percentage_votes)

# Add analysis into single results list
print("Election Results")
results.append(“Total Votes : ” + +str(round(total_votes)))
results.append(str(Candidates, percentage_votes, number_votes)
results.append(“Average Change :” +“$”+str(avg_Chng))
results.append("Winner: " win)

# write the analysis into file