# Election Results Analysis
## Overview:
The purpose of this analysis is to determine the winning candidate for based on election results from three counties namely, Arapahoe, Denver, and Jefferson from the state of Colorado. The python code was written to parse through a csv file that harbors the ballot ID, County and Candidate name, to determine the following

i)	Total number of votes.
ii)	Total number of votes obtained in each county.
iii)	The largest county voter turnout.
iv)	The total number of votes and percentage of votes obtained by each candidate.
v)	Finally, the winning candidate based on the number of votes the individual candidate obtained in the election.

## Total number of votes:
The total number of votes obtained from all the three counties is obtained by initializing the total number of votes to zero and counting the number of entries in the csv file. Based on this calculation, the total number of votes is 369,711.

## Total number of votes obtained in each county:
The total number of votes obtained in each county is obtained by initializing an empty dictionary named county_votes and setting county name to row[1] which indexes the second column in the csv file which refers to the counties. The total county vote count is counted by counting the number of entries for the county name. Based on this calculation, the following results were obtained
i)	Arapahoe: 24,801 or 6.7% of the total votes
ii)	Jefferson: 38,855 or 10.5% of the total votes
iii)	Denver: 306,055 or 82.8% of the total votes.

## The largest county voter turnout:

Based on the calculation, Denver had the highest voter turnout of 306,055 voters that represent 82.8% of the total votes.

## Winning Candidate:
The winning candidate is determined by counting the number of entries for each candidate name for all the three counties. The person which the maximum number of entries or votes is considered the winning candidate. The voters and their percentage votes obtained are listed below:
i)	Charles Casper Stockham: 85,213 votes or 23% of the votes
ii)	Diana DeGette: 272,892 votes or 73.8% of the votes
iii)	Raymon Anthony Doane: 11,606 votes or 3.1% of the votes

Based on the vote count, Diana DeGette is considered the winner for the counties Arapahoe, Denver and Jefferson.
Election Audit Summary:
This code can be used as a template for determining election results for the state and as well nationwide count of popular votes. 

## Modifications to the code:


This code can be utilized to add more counties and to determine if a particular candidate win the state election. 


