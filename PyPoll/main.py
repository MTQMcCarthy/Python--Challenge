#import modules
import os
import csv

#load the file I need
csvpath = os.path.join("Resources", "election_data.csv")
#The total number of votes cast, list of candidates

#create variables
totalVotes = 0
uniqueCandidate = {}
candidatePercent = {}
winnerCount = 0
winner = ""

with open(csvpath, 'r', newline='', encoding='utf-8') as csvfile:
    election_csvreader = csv.DictReader(csvfile, delimiter=',')
    next(election_csvreader, None)

    for row in election_csvreader:
        #determine the total votes
        totalVotes += 1
        #identify the list of unique candidates and tally
        if row["Candidate"] in uniqueCandidate.keys():
            uniqueCandidate[row["Candidate"]] += 1
        else:
            uniqueCandidate[row["Candidate"]] = 1

        #determine % for each candidate by pulling info from items in the uniqueCandidates dictionary
        for name, value in uniqueCandidate.items():
            candidatePercent[name] = round((value/totalVotes) * 100, 1)

        #determine the winner using the uniqueCandidate dictionary 
        for name in uniqueCandidate.keys():
            if uniqueCandidate[name] > winnerCount:
                winner = name
                winnerCount = uniqueCandidate[name]

print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------------------")
for key, value in uniqueCandidate.items():
    print(key + ": " + str(candidatePercent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")



