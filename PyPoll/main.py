#Dependencies
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    votes = 0
    total_candidates = 0

    candidates = []
    candidate_votes = {}
 
    for row in csvreader:
        votes += 1
        total_candidates = row[2]

        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1

    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes:", str(votes))
    print("-------------------------")

    for candidate in candidate_votes:
        candidate_results = (candidate + ": " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
        
        print(candidate_results)

winner = list(candidate_votes.keys())[0]

print("------------------------")
print("Winner: " + str(winner))
print("-------------------------")