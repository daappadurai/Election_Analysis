import csv
import os
file_to_load =('election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_vote = 0
candidate_options = []
candidate_votecount = {}
Winning_candidate = ""
Winning_vote = 0
Winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    header = next(file_reader)
    for row in file_reader:
        total_vote += 1
        candidate_name =row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votecount[candidate_name] = 0
        candidate_votecount[candidate_name] += 1
    for candidate_name in candidate_votecount:
        votes = candidate_votecount[candidate_name]
        vote_percentage = float(votes)/float(total_vote) *100
        print(f"{candidate_name}: received {vote_percentage: .1f} % of the vote")
        if  votes > (Winning_vote) and (vote_percentage > Winning_percentage):
            Winning_vote = votes    
            Winning_percentage = vote_percentage
            Winning_candidate = candidate_name
    print(f"{Winning_candidate}:{Winning_percentage: .1f}% ({Winning_vote:,})\n")

winning_candidate_summary =(
    f".............................\n"
    f"Winner: {Winning_candidate}\n"
    f"Winning_vote :{Winning_vote: ,}\n"
    f"Winning_percentage:{Winning_percentage: .1f}%\n"
    f".............................\n")
print(winning_candidate_summary)




    

    
    
        










