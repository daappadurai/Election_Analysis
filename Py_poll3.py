import csv
file_to_load =('election_results.csv')
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    header = next(file_reader)
    print(header)
   





