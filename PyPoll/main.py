import csv
import os

# Files to load 
file= os.path.join("/Users/yxair/Desktop/NW Bootbcamps/HW/3-Python/Instructions/PyPoll/Resources/election_data.csv")
outputfile= os.path.join("/Users/yxair/Desktop/NW Bootbcamps/HW/3-Python/Instructions/PyPoll/Resources/pypoll.txt")
number_votes = 0
candidate = []
votes = []
name = []

with open(file) as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)

    candidate = []
    for r in csvreader:
        candidate.append(r[2])

    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]
    
    
    for r in candidate_count:
        name.append(r[0])
        votes.append(r[1])

    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]  
total_votes = len(candidate)

Cttl = candidate.count('Correy')
Cpct = int(Cttl) / int(total_votes)

OTttl = candidate.count("O'Tooley")
OTpct = Cttl/ total_votes

LIttl = candidate.count('Li')
LIpct = LIttl/total_votes

KHttl = candidate.count('Khan')
KHpct = KHttl / total_votes


out= (
      f'Election Results\n'
      '-------------------------\n'
      f'Total Votes: {total_votes}\n'
      '-------------------------\n'
      f'Khan: {KHpct:.3%} ({KHttl})\n'
      f'Correy: {Cpct:.3%} ({Cttl})\n'
      f'Li: {LIpct:.3%} ({LIttl})\n'
      f"O'Tooley: {OTpct:.3%} ({OTttl})\n"
      '-------------------------\n'
      f'Winner: {winner_name}\n'
      '-------------------------\n'
)

with open(outputfile, "w") as txt:
       txt.write(out)