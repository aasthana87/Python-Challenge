#Dependencies
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#Variable Lists
date = []
profits_losses = []
change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    rowcount = 0
    net_total = 0

    for row in csvreader:
        
        date.append(row[0])

        profits_losses.append(float(row[1]))

        rowcount += 1
        net_total += int(row[1])

    #Total differences within the "profits/losses" column. Find which dates and values correspond with greatest increase and decrease in revenue.
    for i in range(0,len(profits_losses)):
            change.append(profits_losses[i] - profits_losses[i-1])
            average_change = sum(change)/len(change)

            max_change = round(max(change))
            max_change_date = str(date[change.index(max(change))])

            min_change = round(min(change))
            min_change_date = str(date[change.index(min(change))])
 
    #Print to terminal
    print ("Financial Analysis")
    print("---------------------------")
    print("Total Months:", rowcount)
    print("$", net_total)
    print("Average Change: $", round(average_change))
    print("Greatest Increase in Revenue:",max_change_date,"($",max_change,")")
    print("Greatest Decrease in Revenue:",min_change_date,"($",min_change,")")
    
    
    
    

        

