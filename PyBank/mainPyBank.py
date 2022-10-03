# load dependencies
import os
import csv

# file path to open csv
budget_data = os.path.join( "Resources", "budget_data.csv")

# store variables
total_months = 0
total_profit = 0
initial_rev = 0

# list of dictionary to store variable data
list_change_in_rev = []
month_change_rev = []

# loop to read and create a list of dictionaries for date and profit
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header
    next(csvreader)

    # initialize loop for data
    for rows in csvreader:

    # find the count of months, and total sum of profit/losses
        total_months = total_months + 1
        total_profit = total_profit + int(rows[1])

        #store the months in list for later, will use to see which month had greatest change
        month_change_rev.append(rows[0])

        # start revenue change calculation on 2nd line
        if total_months == 1:
            initial_rev = total_profit
            continue
        else: 
            change_in_rev = int(rows[1]) - int(initial_rev)
            initial_rev = int(rows[1])          
            list_change_in_rev.append(change_in_rev)
        
        # find greatest changes in profit over period
        max_profit = max(list_change_in_rev)
        min_profit = min(list_change_in_rev)

        #find the max profit via index
        index_max_profit = list_change_in_rev.index(max_profit) + 1
        max_month = month_change_rev[index_max_profit]

        #find the min profit via index
        index_min_profit = list_change_in_rev.index(min_profit) + 1
        min_month = month_change_rev[index_min_profit]

    #calc avg change over period and set it as variable
    average_change = round(sum(list_change_in_rev)/len(list_change_in_rev),2)

#--------check in terminal that analysis file is working----------
# print("Financial Analysis")
# print("--------------------")
# print(f'Total Months: {total_months}')
# print(f'Total: {total_profit}')
# #print(sum(list_change_in_rev))
# print(f'Average Change: ${average_change}')
# print(f'Greatest Increase in Profits: {max_month} ${max_profit}')
# print(f'Greatest Decrease in Profits: {min_month} ${min_profit}')

# structure how i want text file to look
analysis = (f'Financial Analysis\n -----------------\n Total Months: {total_months}\n Total: {total_profit}\n Average Change: ${average_change}\n Greatest Increase in Profits: {max_month} ${max_profit}\n Greatest Decrease in Profits: {min_month} ${min_profit}\n' )

# print to see analysis variable works in terminal
print(analysis)


# export as analysis as text file
with open('analysis/PyBank Analysis.txt',"w") as txt_file:
    txt_file.write(analysis)
