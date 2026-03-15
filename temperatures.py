temps = [30, 32, 29, 35, 31, 28]

# how many days are above 30
count = 0
highest = 0
sum = 0
for temp in temps:
    if temp > 30:
        count += 1
    if temp > highest:
        highest = temp
    sum += temp

print(f"Number of days higher than 30: {count}")

# highest temperature
print(f"Highest Temperature: {highest}")

# average temperature
average = sum / len(temps)

print(f"Average Temperatures: {average}")
