steps = [5000, 7200, 6400, 8100, 9000, 4000, 7500]

total_steps = 0
highest = 0

#total steps
for step in steps:
    total_steps += step

print(f"Total Steps: {total_steps}")

#average steps
average = total_steps / len(steps)
print(f"Average Steps: {average}")

#highest steps
for step in steps:
    if step > highest:
        highest = step

print(f"Highest Steps: {highest}")  