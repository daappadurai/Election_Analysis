county_dictionary={"Arapahoe":422829 , "Denver":463353 , "Jefferson":432438}

for county, voters in county_dictionary.items():
     
        print("For County" + county+ ", the number of voters is " +str(voters))

Voting_data =[{"county": "Arapahoe", "registered_voters":433829},
              {"county": "Denver", "registered_voters":463353},
              {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(Voting_data)):
        print(Voting_data[i])
for county_dict in Voting_data:
        for value in county_dict.values():
                print (value)

for county_dict in Voting_data.values():
        print (f"There are {"registered voters"} voters in {"county"})  


        







