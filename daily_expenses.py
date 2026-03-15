expenses = [120, 80, 150, 60, 200]
highest = 0
above = 0
sum = 0
#total expenses
for ex in expenses:
    sum += ex
    if ex > highest:
        highest = ex
    if ex > 100:
        above += 1

print(f"Total Expenses: {sum}")
#highest expense
print(f"Highest Expense: {highest}")
#how many expenses above 100
print(f"Expenses above 100:{above}")