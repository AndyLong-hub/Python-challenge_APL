# this script was written on macOS by Andrew Long
# Python-challenge homework

import csv, os


# financial analysis
def PyBank():
    
    # nested list of csv data [ [month/year, profit/loss], [] ]
    budget_data = []


    # open budget_data.csv
    with open(currDir + '/Resources/budget_data.csv', 'r') as csv_data:

        # iterate through data and store in list
        for line in csv.reader(csv_data):
            budget_data.append(line)


    # remove header from list
    budget_data.pop(0)


    # count total months
    total_months = len(budget_data)


    # sum profit/loss for all months
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



    # format output
    output = (
        f"Financial Analysis from budget_data.csv\n"
        "------------------\n"
        f"Total months: {total_months}\n"
        f"Total: ${profit_loss:,}\n"
        f"Average change: ${avg_change:,.2f}\n"
        f"Greatest Increase in Profits: {max_month}, ${max_profit:,}\n"
        f"Greatest Decrease in Profits: {min_month}, ${min_profit:,}\n"
        )
    

    return output


def PyPoll():

    # nested list of csv data
    election_data = []


    # open election_data.csv
    with open(currDir + '/Resources/election_data.csv', 'r') as csv_data:
        

        # warn user of delay (lots of data to load)
        print("Loading data. This will take a few moments. . . ")

        
        # iterate through data and store in list
        for line in csv.reader(csv_data):
            election_data.append(line)


    # remove header from list
    election_data.pop(0)


    # total number of votes cast
    total_votes = len(election_data)

    
    # complete list of candidates who received votes
    candidates = set()
    print("Identifying candidates. . . ")
    for row in election_data:
        candidates.add(row[2])


    # store candidate analysis in dictionary
    c_analysis = {}
    for c in candidates:

        # store analysis output in list for each candidate key
        c_analysis[c] = []


    # percentage of votes each candidate won
    for row in election_data:
        

    ##The total number of votes each candidate won
    ##
    ##
    ##The winner of the election based on popular vote.
    ##
    ##
    ##
    ##
    ##As an example, your analysis should look similar to the one below:
    ##Election Results
    ##-------------------------
    ##Total Votes: 3521001
    ##-------------------------
    ##Khan: 63.000% (2218231)
    ##Correy: 20.000% (704200)
    ##Li: 14.000% (492940)
    ##O'Tooley: 3.000% (105630)
    ##-------------------------
    ##Winner: Khan
    ##-------------------------
    ##
    ##
    ##In addition, your final script should both print the analysis to the terminal and export a text file with the results.


    
    return election_data



def outputFile(file_name, output):

    # export to .txt file in Analysis folder
    file_location = currDir + f"/Analysis/{file_name}"
    txt_output = open(file_location,"w")
    txt_output.write(output)
    txt_output.close()

    print(f"File was saved to:\n{file_location}")
    
    return None



# current working directory
currDir = os.getcwd()


input("Press any button to run PyBank. . . ")

# run PyBank script
finance_analysis = PyBank()
print(f"Running PyBank script. . .\n\n{finance_analysis}")
outputFile("PyBank", finance_analysis)
print("PyBank completed successfully!\n")

input("Press any button to run PyPoll. . . \n")


# run PyPoll script
election_results = PyPoll()





