# modules imported:
import csv

# global variables
csv_path = "election_data.csv"
total_votes = 0
set_of_candidates = set()
list_of_candidates = []
total_percentages = {}
winner = ["", 0]

# setting up to read through csv file
with open(csv_path, "r") as f:
    reader = csv.reader(f)
    next(reader)

    # looping through csv file for: total votes, Candidates voted for, and tallying votes
    for row in reader:
        total_votes = total_votes + 1
        set_of_candidates.add(str(row[2]))
        if row[2] in total_percentages:
            total_percentages[row[2]] += 1
        else:
            total_percentages[row[2]] = 1

    # converting my set of candidates to a list to use more easily in the printing and determining a winner
    list_of_candidates = list(set_of_candidates)

    # small loop for figurig out who had the most votes
    for candidate in list_of_candidates:
        if total_percentages[candidate] > winner[1]:
            winner[0] = candidate
            winner[1] = total_percentages[candidate]

    # printing all the outputs
    print(f"Total number of votes: {total_votes}")
    print(f"Total number of candidates: {', '.join(list_of_candidates)}")
    print(
        f"Total percentage/count of votes for {list_of_candidates[0]}: {(total_percentages[list_of_candidates[0]]/total_votes) * 100}%, {total_percentages[list_of_candidates[0]]}"
    )
    print(
        f"Total percentage/count of votes for {list_of_candidates[1]}: {(total_percentages[list_of_candidates[1]]/total_votes) * 100}%, {total_percentages[list_of_candidates[1]]}"
    )
    print(
        f"Total percentage/count of votes for {list_of_candidates[2]}: {(total_percentages[list_of_candidates[2]]/total_votes) * 100}%, {total_percentages[list_of_candidates[2]]}"
    )
    print(
        f"Total percentage/count of votes for {list_of_candidates[3]}: {(total_percentages[list_of_candidates[3]]/total_votes) * 100}%, {total_percentages[list_of_candidates[3]]}"
    )
    print(f"The winner of the election: {winner[0]}")

# function and function call to print results to a .txt file
def put_in_text():
    return f"""Total number of votes: {total_votes}\n===========================\n
Total number of candidates: {', '.join(list_of_candidates)}\n===========================\n
Total percentage/count of votes for {list_of_candidates[0]}: {(total_percentages[list_of_candidates[0]]/total_votes) * 100}%, {total_percentages[list_of_candidates[0]]}\n===========================\n
Total percentage/count of votes for {list_of_candidates[1]}: {(total_percentages[list_of_candidates[1]]/total_votes) * 100}%, {total_percentages[list_of_candidates[1]]}\n===========================\n
Total percentage/count of votes for {list_of_candidates[2]}: {(total_percentages[list_of_candidates[2]]/total_votes) * 100}%, {total_percentages[list_of_candidates[2]]}\n===========================\n
Total percentage/count of votes for {list_of_candidates[3]}: {(total_percentages[list_of_candidates[3]]/total_votes) * 100}%, {total_percentages[list_of_candidates[3]]}\n===========================\n
The winner of the election: {winner[0]}"""


output = put_in_text()
file = open("results.txt", "w")
file.write(output)
file.close()
