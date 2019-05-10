# modules imported
import csv


# global variables
csv_path = "budget_data.csv"
total_months = 0
net_total = 0
array_of_diferrence = []
average_PL = 0
greatest_increase = [0, 0]  # date and amount
greatest_decrease = [0, 0]  # date and amount
prev_row = 867884

# preparing to read through csv doc
with open(csv_path, "r") as f:
    reader = csv.reader(f)
    next(reader)

    # looping through csv file looking for: total months, net total, change from month to month, finding greatest increase and decrease
    for row in reader:
        total_months += 1
        net_total += int(row[1])
        array_of_diferrence.append(int(row[1]) - int(prev_row))
        if (int(row[1]) - int(prev_row)) > int(greatest_increase[1]):
            greatest_increase = [row[0], (int(row[1]) - int(prev_row))]
        if (int(row[1]) - int(prev_row)) < int(greatest_decrease[1]):
            greatest_decrease = [row[0], (int(row[1]) - int(prev_row))]
        prev_row = row[1]

    # printing all the outputs
    print(f"Total number of months: {total_months}")
    print(f"Total net amount of Profit/Losses: {net_total}")
    print(
        f"Average change in Profit/Losses: {int(sum(array_of_diferrence) / (len(array_of_diferrence)-1))}"
    )
    print(
        f"The greatest increase in profits:\n   Date: {greatest_increase[0]}\n   Amount: {greatest_increase[1]}"
    )
    print(
        f"The greatest decrease in losses:\n   Date: {greatest_decrease[0]}\n   Amount: {greatest_decrease[1]}"
    )
    print(net_total / total_months)
# function and function call to print results to a .txt file
def put_in_text():
    return f"""Total number of months: {total_months}\n===========================\n
Total net amount of Profit/Losses: {net_total}\n===========================\n
Average change in Profit/Losses: {int(sum(array_of_diferrence) / len(array_of_diferrence))}\n===========================\n
The greatest increase in profits:\n   Date: {greatest_increase[0]}\n   Amount: {greatest_increase[1]}\n===========================\n
The greatest decrease in losses:\n   Date: {greatest_decrease[0]}\n   Amount: {greatest_decrease[1]}"""


output = put_in_text()
file = open("results.txt", "w")
file.write(output)
file.close()
