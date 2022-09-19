import os
import csv

election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

vote_count = 0                  # initialize vote counter
candidate_options = []          # list for candidate options     
candidate_vote_count = {}       # candidate vote counter
winner_vote_count = 0           # for tracking vote count of winner
candidate_vote_percent = 0      # for tracking vote percentage for the winner
winner = ""

with open(election_data, encoding='utf-8') as csvfile:      # opens election results and reads the file
    csvreader = csv.reader(csvfile, delimiter=',')          
    cvs_header = next(csvreader)                            # reads the header row

    for row in csvreader:
        vote_count += 1
        candidate = row[2]

        if candidate not in candidate_options:
            candidate_options.append(candidate)
            candidate_vote_count[candidate] = 0
        
        candidate_vote_count[candidate] += 1


    



# printing lines
print("Election Results")
print("-"*20)
print(f"Total Votes: {vote_count}")
# print(f"Total Votes: {len(vote_counter)}")
print("-"*20)
