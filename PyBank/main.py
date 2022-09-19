import os
import csv

# insert code to show where the csv is here - according to terminal the path starts from Python-Challenge folder
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

# creating variables to store the data I need to report on
month_count = [] # generates a list named months
pnl = [] # generates a list named pnl
pnl_change = [] # generates a list named pnl_change

# open and read csv file'
with open(budget_data, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # read the header row first
    csv_header = next(csvreader)
    
    # print(f"Header: {csv_header}" - we arent really printed so not necessary for the hw
    # now i want to read each row of data after the header and iterate through the values/add them to empty lists
    for row in csvreader:
        # add month to empty list
        month_count.append(row[0])
        # add profit to empty list
        pnl.append(int(row[1]))
    
    for i in range(len(pnl)-1):
        pnl_change.append(pnl[i+1]-pnl[i])

greatest_increase = max(pnl_change)
greatest_decrease = min(pnl_change)

# find the date of these increases
increase_date = pnl_change.index(max(pnl_change))+1
decrease_date = pnl_change.index(min(pnl_change))+1

# find the average monthly change
average = round(sum(pnl_change)/len(pnl_change),2)

      
print("Financial Analysis")
print("-"*20)
print(f"Total Months: {len(month_count)}")
print(f"Total PNL: ${sum(pnl)}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {month_count[increase_date]} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {month_count[decrease_date]} ${greatest_decrease}")

output_file = os.path.join("PyBank", "Resources", 'output.txt')
with open(output_file, "w") as new:
    msg = (
      f"Financial Analysis\n"
      f"-----------------------\n"
      f"Total Months: {len(month_count)}"
      f"Total PNL: ${sum(pnl)}"
      f"Average Change: ${average}"
      f"Greatest Increase in Profits: {month_count[increase_date]} ${greatest_increase}"
      f"Greatest Decrease in Profits: {month_count[decrease_date]} ${greatest_decrease}"  
    )
    new.write(msg)