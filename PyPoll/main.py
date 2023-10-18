# Import dependencies
import os, csv
from pathlib import Path 

# Assign file location with the pathlib library
csv_file_path = Path("Resources", "election_data.csv")

# Declare Variables 
total_votes = 0 
candidates = []
CanVotes = {}
winningCount = 0
winningCandidate = ""


# Open csv in default read mode with context manager
with open(csv_file_path,newline="", encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

     # read the header row 
    header = next(csvreader)
    # move      

    # for each row
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes += 1



        # Check to see if the candidates name is found in our list of votes
        if row[1] not in candidates:
            # if the candidates is not in the list, add the candidate to the list 
            candidates.append(row[1])

            # add the value to the dictonary as well
            CanVotes[row[1]] = 1

        else:
            CanVotes[row[1]] += 1

voteOutput = ""

for candidate in CanVotes:
    votes = CanVotes.get(candidate)
    votePct = (float(votes) / float(total_votes)) *100
       
    voteOutput += f"\t{candidate}: {votePct:.2f}% /n"

    # compare the votes to the winning count
    if votes > winningCount:
        # update the votes to be the new winning count
        winningCount = votes
        # update the winning candidate 
        winningCandidate = candidate

winningCandidateOutput = f"\t\tWinner: {winningCandidate}\n----------------------------"


# Output files
output_file = Path("analysis", "Election_Results_Summary.txt")

# create an output variable to hold the output 
output = (
    f"\n\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes:,} \n"
    f"----------------------------\n"
    f"{voteOutput} \n"
    f"----------------------------\n"
    f"{winningCandidateOutput}"
)

# display the output to the console / terminal
print(output)

with open(output_file, "w") as textFile:
    # write the ouput to the text file 
    textFile.write(output)