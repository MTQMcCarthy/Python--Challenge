#import modules
import os
import csv

#load the file I need
csvpath = os.path.join("Resources", "budget_data.csv")
#pathout = os.path.join("Resources", "budget_analysis.txt")

#Variables and values so I can track them 
totalMonths = 0
totalProfitLoss = 0
avgProfitLoss = 0
greatestIncrease = ["",0]
greatestDecrease = ["",0]
#revenue_change = 0
#revenue_change_list = []
#month_of_change = []
#greatestDecrease = ["", 99999999999]

#Read the budget_data.csv file
with open(csvpath) as budgetData:
    reader = csv.DictReader(budgetData)

#calculate the total number of months included in the dataset
    for row in reader:
        
        #count total months in csv file
        totalMonths = totalMonths + 1

print("Total Months: {totalMonth}\n")