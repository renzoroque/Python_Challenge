# File: main.py

import os
import csv
csvpath = os.path.join('..','Resources','budget_data.csv')
net_change_l = []
month_of_change = []

with open(csvpath) as csvfile:
    PyBank = csv.reader(csvfile, delimiter=',')
    csv_header = next(PyBank)
    total_months = 0
    total_profits = 0
    net_change = 0
    profit = 0
               
    for row in PyBank:
        total_months = total_months + 1   
        value = int(row[1])
        total_profits = total_profits + value
        month_of_change.append(str(row[0]))
        #Calculate the average in changes
        if net_change != 0:
            profit = value
            net_change = profit - net_change
            net_change_l.append(net_change)
            net_change = value
        #Setting value for first row
        elif net_change == 0:
            net_change = value
        
month_of_change.pop(0)                
average_change = sum(net_change_l)/(len(net_change_l))
average_change = round(average_change, 2)
#Max Profit and Month
max_profit = max(net_change_l)
max_month = month_of_change[net_change_l.index(max_profit)]

#Min Profit and Month
min_profit = min(net_change_l)
min_month = month_of_change[net_change_l.index(min_profit)]

print('''Financial Analysis
------------------''')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profits}')
print(f'Averange Change: ${average_change}')
print(f'Greatest Increase in Profits: ${max_profit} on {max_month}')
print(f'Greatest Decrease in Profits: ${min_profit} on {min_month}')


PyBank_txt = os.path.join("..","Analysis", "budget_data.txt")
with open(PyBank_txt, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {total_months}\n")
    outfile.write(f"Total:  ${total_profits}\n")
    outfile.write(f"Average Change:  ${average_change}\n")
    outfile.write(f"Greatest Increase in Profits:  ${max_profit} on {max_month}\n")
    outfile.write(f"Greatest Decrease in Losses:  ${min_profit} on {min_month}\n")