# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The total net amount of "Profit/Losses" over the entire period

# The average change in "Profit/Losses" between months over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


import csv

csv_path = 'budget_data.csv'
total_months = 0
net_total = 0
array_of_diferrence =[]
average_PL = 0
greatest_increase = [0,0] #date and amount
greatest_decrease = [0,0] #date and amount
prev_row = 867884

with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total_months = total_months +1
        net_total = net_total + int(row[1])
        array_of_diferrence.append(int(row[1]) - int(prev_row))
        if (int(row[1]) - int(prev_row)) > int(greatest_increase[1]):
            greatest_increase = [row[0], row[1]]
        if (int(row[1]) - int(prev_row)) < int(greatest_decrease[1]):
            greatest_decrease = [row[0], row[1]]
        prev_row = row[1]
    print(f"Total number of months: {total_months}")
    print(f"Total net amount of Profit/Losses: {net_total}")
    print(f"Average change in Profit/Losses: {int(sum(array_of_diferrence) / len(array_of_diferrence))}")
    print(f"The greatest increase in profits:\n   Date: {greatest_increase[0]}\n   Amount: {greatest_increase[1]}")
    print(f"The greatest decrease in losses:\n   Date: {greatest_decrease[0]}\n   Amount: {greatest_decrease[1]}")

def put_in_text():
    return f"""Total number of months: {total_months}\n===========================\n
Total net amount of Profit/Losses: {net_total}\n===========================\n
Average change in Profit/Losses: {int(sum(array_of_diferrence) / len(array_of_diferrence))}\n===========================\n
The greatest increase in profits:\n   Date: {greatest_increase[0]}\n   Amount: {greatest_increase[1]}\n===========================\n
The greatest decrease in losses:\n   Date: {greatest_decrease[0]}\n   Amount: {greatest_decrease[1]}\n===========================\n"""
output = put_in_text()
file = open("results.txt","w")
file.write(output)
file.close()
