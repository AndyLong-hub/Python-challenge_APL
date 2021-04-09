# this script was written on macOS by Andrew Long
# Python-challenge homework

import csv, os

# current working directory
currDir = os.getcwd()


# nested list of csv data [ [month/year, profit/loss], [] ]
budget_data = []


# open budget_data.csv
with open(currDir + '/Resources/budget_data.csv', 'r') as csv_data:
    csv_reader = csv.reader(csv_data)

    # iterate through data and store in list
    for line in csv_reader:
        budget_data.append(line)


# remove header from list
budget_data.pop(0)


# count total months
total_months = len(budget_data)


# sum profits/losses
profit_loss = 0
for row in budget_data:
    profit_loss += int(row[1])



# Calculate the changes in "Profit/Losses" over the entire period
change = []
for i in range(0, len(budget_data)-1):
    diff = int(budget_data[i+1][1]) - int(budget_data[i][1])
    change.append(diff)


# average change in profit/loss
avg_change = sum(change) / len(change)


# identify month with the greatest increase in profit
max_month = budget_data[change.index(max(change))+1][0]
max_profit = max(change)


# identify greatest decrease in profits (month and amount)
min_month = budget_data[change.index(min(change))+1][0]
min_profit = min(change)


# format output and print for verification
output = (
    "Financial Analysis\n"
    "------------------\n"
    f"Total months: {total_months}\n"
    f"Total: ${profit_loss:,}\n"
    f"Average change: ${avg_change:,.2f}\n"
    f"Greatest Increase in Profits: {max_month}, ${max_profit:,}\n"
    f"Greatest Decrease in Profits: {min_month}, ${min_profit:,}\n"
    )

print(output)

input("Press any button to export Financial Analysis to a .txt file: ")



# if user approves output, then export to .txt file in Analysis folder

