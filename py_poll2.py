import os
file_to_load = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load, 'w') as txt_file:
    txt_file.write("Hello World, ")
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson, ")
    txt_file.close()


