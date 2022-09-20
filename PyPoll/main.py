import os
import csv

election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

vote_count = 0                  # total_votes
candidate_options = []          # candidate_options   
candidate_vote_count = {}       # candidate_votes
winner_vote_count = 0           # winning_count
winner_vote_percent = 0         # winning_percentage
winner = ""                     # winning_candidate

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

# now saving results to the text file
output_file = os.path.join("PyPoll", "Analysis", "Analysis.txt")
with open(output_file, 'w') as new:
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {vote_count}\n"
        f"---------------------\n"
    )
    print(election_results, end="")
    new.write(election_results)

    for candidate in candidate_vote_count:
        votes = candidate_vote_count[candidate]
        vote_percent = float(votes) / float(vote_count) * 100
        candidate_result = (f"{candidate}: {vote_percent:.3f}% ({votes})\n"
        )
        print(candidate_result)
        new.write(candidate_result)

        # find winning vote count, candidate and percentage
        if (votes > winner_vote_count) and (vote_percent > winner_vote_percent):
            winner_vote_count = votes
            winner = candidate
            winner_vote_percent = vote_percent
    
    msg = (
        f"--------------------\n"
        f"Winner: {winner}\n"
    )

    print(msg)
    new.write(msg)


# instead of using if/in structure, look to use a dictionary (key)

# # printing lines
# print("Election Results")
# print("-"*20)
# print(f"Total Votes: {vote_count}")
# # print(f"Total Votes: {len(vote_counter)}")
# print("-"*20)
