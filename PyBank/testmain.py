# import modules
import csv
import os

#sources to read revenue data file 
fileload = os.path.join("Resources", "budget_data.csv")

# file to hold the output of budget analysis
outputFile = os.path.join("analysis", "Financial Analysis.txt")

# variables 
totalMonths = 0
profits = 0
profit_change = []
months = []


# read the csv file 
with open(fileload) as budgetData:
    #create a csv reader object 
    csvreader = csv.reader(budgetData)

    # read the header row 
    header = next(csvreader)
    # move to the first row 
    firstRow = next(csvreader)



     # increment the count of total months
    totalMonths += 1

    # add on to the total amount of profits
        # profits is in index 1 
    profits += float(firstRow[1])

    # establish the pervious budget
    previousBudget = float(firstRow[1])



    for row in csvreader:
        # increment the count of total months
        totalMonths += 1

        # add on to the total amount of profits
        # profits is in index 1 
        profits += float(row[1])

        # calculate the net change 
        netchange = float(row[1]) - previousBudget
        # add on to the list of profit change 
        profit_change.append(netchange)

        # add the first month that a change occurred 
            # month is in index 0
        months.append(row[0])

        # update the previous budget
        previousBudget = float(row[1])

# Calculate the average net change per month
averageChangePerMonth = sum(profit_change) / len(profit_change)

greatestIncrease = [months[0], profit_change[0]]
greatestDecrease = [months[0], profit_change[0]]

# use loop to calculate the index of the greatest and least profit change 
for pc in range(len(profit_change)):
    # calculate the greatest increase and decrease 
    if(profit_change[pc] > greatestIncrease[1]):
        # if the value is greater than the greatest increase, that value becomes the new greatest increase
        greatestIncrease[1] = profit_change[pc]
        # update the month 
        greatestIncrease[0] = months[pc]

    if(profit_change[pc] < greatestDecrease[1]):
        # if the value is less than the greatest decrease, that value becomes the new greatest decrease
        greatestDecrease[1] = profit_change[pc]
        # update the month 
        greatestDecrease[0] = months[pc]



# start generating the output 
output = (
    f"\nFinancial Analysis \n"
    f"----------------------------\n"
    f"\tTotal Months = {totalMonths} \n"
    f"\tTotal Profits = ${profits:,.2f} \n"
    f"\tAverage Change = ${averageChangePerMonth:,.2f} \n"
    f"\tGreatest Increase = {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f} \n"
    f"\tGreatest Decrease = {greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f} \n"
    )


# print the output 
print(output)

# export the output to the output text file 
with open(outputFile, "w") as textFile:
    textFile.write(output)