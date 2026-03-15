expenses = [120, 80, 150, 60, 200]
total = 0
highest = 0
# total spent
for ex in expenses:
    total += ex

print(f"Total Spent: {total}")

# average expense
average = total / len(expenses)
print(f"Average Expense: {average}")

# highest expense
for ex in expenses:
    if ex > highest:
        highest = ex

print(f"Highest Expense: {highest}")