import os
import csv

csvpath = "C:/Users/Walid/Documents/Columbia/COLNYC20190716DATA/02-Homeworks/03-Python/Instructions/PyPoll/Resources/election_data.csv"

# variables
total_votes = 0
candidate = ""
candidate_list = []
vote_list = []
percent_list = []
winner = ""

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    # Skip the first header
    csv_header = next(csvreader)  
    
    # Read each row of data after the header
    for row in csvreader:

        total_votes += 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_list.append(1)
        else:
            vote_list[candidate_list.index(row[2])] += 1

    
    # Percent of vote            
percent_list = [(100/total_votes) * x for x in vote_list]

# The winner
winner = candidate_list[vote_list.index(max(vote_list))]

# Print the results      
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for x in candidate_list:
    print(x + ": " + str(format(percent_list[candidate_list.index(x)], '.3f')) 
        + "% (" + str(vote_list[candidate_list.index(x)]) + ")")
    
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")




