import os
import csv

total_votes = 0
percentage_votes = []
candidate_votes = []
Candidate = []
votes = []


with open(csvpath) as csvfile:
    PyPoll = csv.reader(csvfile, delimiter=',')
    csv_header = next(PyPoll)

    for row in PyPoll:  
        total_votes += 1
        
        if row[2] not in Candidate:
            Candidate.append(row[2])
            
        votes.append(row[2])
        
    for candidate in Candidate:
        candidate_votes.append(votes.count(candidate))
        percentage_votes.append(round(votes.count(candidate)/total_votes*100,3))
                                       
winner = Candidate[candidate_votes.index(max(candidate_votes))]
                                      
print(f'Election Results!!!')
print(f'-----------------')
print(f'Total Votes: {total_votes}')
print(f'-----------------')
for i in range(len(Candidate)):
    print(f'{Candidate[i]}: {percentage_votes[i]}% ({candidate_votes[i]})')
print(f'-----------------')
print(f'Winner: {winner}')

PyPoll_txt = os.path.join("poll_data.txt")
with open(PyPoll_txt, "w") as outfile:

    outfile.write(f"Elections Results!!!\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Votes:  {total_votes}\n")
    outfile.write("----------------------------\n")
    for i in range(len(Candidate)):
        outfile.write(f"{Candidate[i]}: {percentage_votes[i]}% ({candidate_votes[i]})\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("----------------------------\n")