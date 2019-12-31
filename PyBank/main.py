#import modules
import os
import csv

#load the file I need
csvpath = os.path.join("Resources", "budget_data.csv")

#create variables
totalMonths = 0
totalProfitLoss = 0
pastProfitLoss = 0
greatestIncrease = 0
greatestDecrease = 99999999999

#create lists to store revenue change
profitChange = []
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    next(budget_csvreader, None)
    
    for row in budget_csvreader:
        #determine total months in file
        totalMonths = totalMonths + 1
        
        #determine total porifts/losses
        totalProfitLoss = totalProfitLoss + (int(row[1]))
        
        #create a variable that will tally the change
        monthlyProfitChange = int(row[1]) - pastProfitLoss
        pastProfitLoss = int(row[1])
        
        #create a list to store the changes 
        profitChange.append(monthlyProfitChange)
        
        #determine the average change in revenue
        avgprofitChange = round(sum(profitChange)/totalMonths)
        
        #determine the greatest increase in revenue
        if (monthlyProfitChange > greatestIncrease):
            greatestIncreaseMonth = row[0]
            greatestIncrease = monthlyProfitChange 
        
        #determine the greatest decrease in revenue
        if (monthlyProfitChange < greatestDecrease):
            greatestDecreaseMonth = row[0]
            greatestDecrease = monthlyProfitChange

#varible to hold results and use f-strings for formatting
Results = (
f"Financial analysis\n"
f"------------------\n"
f"Total months: {totalMonths}\n"
f"Total profits or losses: ${totalProfitLoss:,}\n"
f"Average change in profits or losses: ${avgprofitChange:,}\n"
f"Greatest increase in profits was ${greatestIncrease:,} seen in {greatestIncreaseMonth}\n"
f"Greatest decrease in profits was ${greatestDecrease:,} seen in {greatestDecreaseMonth}\n")
print(Results)

# Set variable for output file
pathout = os.path.join("Resources", "results.txt")

#  Open the output file
with open(pathout, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Total months", "Total profits", "Average Change", "Greatest Increase",
                     "Greatest Decrease"])

    # Write in results
    writer.writerows(Results)
