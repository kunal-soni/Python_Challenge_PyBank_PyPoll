import os
import csv
csvpath = os.path.join('election_data.csv')
# Declare variables
totalVotes = 0
# Declare lists to store Names, votes and vote percent
candidateName = []
candidateVotes = []
candidateVotePercent = []
winner = ""
# Another list needed to store index
cIndex = []
# Declare Flag to check if new candidate and declare current candidate variable
newCandidateFlag = "y"
currentCandidate = ""
cIndexVal = 0
#Reading using CSV module
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first 
    csv_header = next(csvreader)
    # Loop through each row in csv file
    for row in csvreader:
        totalVotes += 1
        currentCandidate = row[2]
        # Check if current candidate is in candidateName list
        if currentCandidate in candidateName:
            newCandidateFlag = 'n'
            cIndexVal = candidateName.index(currentCandidate)
            candidateVotes[cIndexVal] += 1
        else:
            newCandidateFlag = 'y'
            candidateName.append(currentCandidate)
            candidateVotes.append(1)
            cIndex.append(cIndexVal + 1)
            # End loop
# Calculate Candidate Votes Percentage
j=0
winner = candidateName[j]
winnerVotes = candidateVotes[j]
# Loop to find winner based on maximum votes
# Lists candidateVotes and candidateName have same number of elements
for j in range(len(candidateVotes)):
    #candidateVotePercent.append(candidateVotes[j]*100.0/totalVotes)
    candidateVotePercent.append('%.3f' %(candidateVotes[j]*100.0/totalVotes))
    if(candidateVotes[j] > winnerVotes):
        winner = candidateName[j]
# Print output on screen
print(f'''Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------''')
# Loop to print each candidate with their votes
i = 0
for i in range(cIndexVal+1):
    print(f"{candidateName[i]}: {candidateVotePercent[i]}% ({candidateVotes[i]})")
# Print Winner
print(f"""-------------------------
Winner: {winner}
-------------------------""")
# Print output to csv file
cleaned_csv = zip(candidateName,candidateVotePercent,candidateVotes)
# Set variable for output file
output_file = os.path.join("Poll_Results.csv")
#  Open the output file
with open(output_file,'w',newline='') as datafile:
    writer = csv.writer(datafile)
    
    # Write Heading
    writer.writerow(["Election Results"])
    writer.writerow(["Total Votes",totalVotes])
    # Write the header row
    writer.writerow(["Name", "Percent", "Total Votes"])
    # Write in zipped rows
    writer.writerows(cleaned_csv)
    # Write Winner
    writer.writerow(["Winner",winner])