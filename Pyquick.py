import csv
file_to_load =('election_results.csv')
Total_vote = 0
Candidate_options =[]
with open(file_to_load,'r') as election_data:
    file_reader = csv.reader(election_data)
    header = next(file_reader)
print(header)
