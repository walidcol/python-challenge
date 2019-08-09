import os
import csv

#csvpath  = os.path.join("..", "PyBank","Resources", "budget_data.csv") 

csvpath = "C:/Users/Walid/Documents/Columbia/COLNYC20190716DATA/02-Homeworks/03-Python/Instructions/PyBank/Resources/budget_data.csv"

# set variables
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
month_change = 0
total_month_change = 0
average_month_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_increase_month = ""


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip the header row
    csv_header = next(csvreader)

# Read each row of data after the header

    for row in csvreader:
    
        #get total months
        total_months += 1

        #get net profit/losses
        total_profit_loss += int(row[1])

        # calculate the change in profit/loss between months
        if total_months > 1:
            month_change = int(row[1]) - prev_profit_loss

        # add up the total monthly change, used later to calculate average
        total_month_change += month_change

        # set profit/loss value for previous month
        prev_profit_loss = int(row[1])

        # calculate greatest increase in profits
        if month_change > greatest_increase:
            greatest_increase = month_change
            greatest_increase_month = row[0]

     # calculate greatest decrease in losses
        if month_change < greatest_decrease:
            greatest_decrease = month_change
            greatest_decrease_month = row[0]

    # calculate average change between months   

        average_month_change = total_month_change / (total_months + 1)

    
print("Financial Analyst")
print("------------------")
print("Total Months : " +str(total_months))
print("Total : $ " +  str(total_profit_loss))
print("Average Change : $ " +str(average_month_change))
print("Greatest Increase in Profits : "  + greatest_increase_month + " ($" + str(greatest_increase) + ")")
print("Greatest Decreases in Losses : "  + greatest_decrease_month + " ($" + str(greatest_decrease) + ")")


