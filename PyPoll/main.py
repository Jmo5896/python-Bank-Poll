# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import csv

csv_path = 'election_data.csv'
total_votes = 0
list_of_candidates = set()
total_percentages = {}

with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total_votes = total_votes + 1
        list_of_candidates.add(str(row[2]))
        if row[2] in total_percentages:
            total_percentages[row[2]] += 1
        else:
            total_percentages[row[2]] = 1
    print(f"Total number of votes: {total_votes}") 
    print(f"Total number of candidates: {', '.join(list(list_of_candidates))}")
    print(f"Total percentage of votes for Correy: {(total_percentages['Correy']/total_votes) * 100}%")
    print(f"Total percentage of votes for Khan: {(total_percentages['Khan']/total_votes) * 100}%")
    print(f"Total percentage of votes for Li: {(total_percentages['Li']/total_votes) * 100}%")
    print(f"Total percentage of votes for O'Tooley: {(total_percentages["O'Tooley"]/total_votes) * 100}%")
def put_in_text():
    return f"""hello world"""

output = put_in_text()
file = open("results.txt","w")
file.write(output)
file.close()