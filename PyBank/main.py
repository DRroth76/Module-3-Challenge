# imports modules needed
import csv

# sets file path
budget_csv = r'C:\Data Analysis Bootcamp\Module 3\cloned_module3challenge_files\Module-3-Challenge\PyBank\Resources\budget_data.csv'
budget_txt = r'C:\Data Analysis Bootcamp\Module 3\cloned_module3challenge_files\Module-3-Challenge\PyBank\analysis\analysis_results.txt'

# establish lists
months = []
money_amounts = []

# to open the CSV file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    data = list(csvreader)

# establishing variables
    number_of_months = 0
    sum_of_profit = 0
    previous_money_amount = 0
    change_in_profit = 0
    total_change_in_profit = 0
    month_of_max_increase = ''
    month_of_max_decrease = ''
    max_increase = 0
    max_decrease = 0

# for loop to pull data 
    for row in data:
        month = str(row[0])
        money_amount = int(row[1])

        months.append(month)
        money_amounts.append(money_amount)

        sum_of_profit += money_amount
        number_of_months += 1
        
    # if statements to find total change in profit, max increase, and max decrease
        if number_of_months > 1:
            change_in_profit = money_amount - previous_money_amount
            total_change_in_profit += change_in_profit
        
            if change_in_profit > max_increase:
                max_increase = change_in_profit
                month_of_max_increase = month

            if change_in_profit < max_decrease:
                max_decrease = change_in_profit
                month_of_max_decrease = month
        
        previous_money_amount = money_amount

    average_change = total_change_in_profit / (number_of_months - 1)

# print financial analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {number_of_months}")
print(f"Total: ${sum_of_profit}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {month_of_max_increase} (${max_increase})")
print(f"Greatest Decrease in Profits: {month_of_max_decrease} (${max_decrease})")

# to print to text file
with open(budget_txt, "w") as text_file:
    output = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {number_of_months}\n"
        f"Total: ${sum_of_profit}\n"
        f"Average Change: ${round(average_change, 2)}\n"
        f"Greatest Increase in Profits: {month_of_max_increase} (${max_increase})\n"
        f"Greatest Decrease in Profits: {month_of_max_decrease} (${max_decrease})\n"
        )
    text_file.write(output)