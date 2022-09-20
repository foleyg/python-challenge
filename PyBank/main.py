import os
import csv

budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

month_count = [] 
pnl = [] 
pnl_change = [] 

with open(budget_data, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        month_count.append(row[0])
        pnl.append(int(row[1]))
    
    for i in range(len(pnl)-1):
        pnl_change.append(pnl[i+1]-pnl[i])

greatest_increase = max(pnl_change)
greatest_decrease = min(pnl_change)

increase_date = pnl_change.index(greatest_increase)+1
decrease_date = pnl_change.index(greatest_decrease)+1

average = round(sum(pnl_change)/len(pnl_change),2)

      
print("Financial Analysis")
print("-"*25)
print(f"Total Months: {len(month_count)}")
print(f"Total PNL: ${sum(pnl)}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {month_count[increase_date]} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {month_count[decrease_date]} ${greatest_decrease}")

output_file = os.path.join("PyBank", "Analysis", 'PyBankAnalysis.txt')
with open(output_file, "w") as new:
    msg = (
      f"Financial Analysis\n"
      f"-----------------------\n"
      f"Total Months: {len(month_count)}\n"
      f"Total PNL: ${sum(pnl)}\n"
      f"Average Change: ${average}\n"
      f"Greatest Increase in Profits: {month_count[increase_date]} ${greatest_increase}\n"
      f"Greatest Decrease in Profits: {month_count[decrease_date]} ${greatest_decrease}\n"  
    )
    new.write(msg)