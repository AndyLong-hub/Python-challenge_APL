##The total number of months included in the dataset
##
##
##The net total amount of "Profit/Losses" over the entire period
##
##
##Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
##
##
##The greatest increase in profits (date and amount) over the entire period
##
##
##The greatest decrease in losses (date and amount) over the entire period

## Output example:
##Financial Analysis
##----------------------------
##Total Months: 86
##Total: $38382578
##Average  Change: $-2315.12
##Greatest Increase in Profits: Feb-2012 ($1926159)
##Greatest Decrease in Profits: Sep-2013 ($-2196167)

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
print("Removing header: ")
print(budget_data.pop(0))
print()


# count total months
print(len(budget_data))

# sum profits/losses

# calculate average profit/loss

# identify greatest increase in profits (month and amount)

# identify greatest decrease in profits (month and amount)

# format output and print for verification

# if user approves print, then export output in .txt file in Analysis folder

