water = [1.5, 2.0, 1.8, 2.2, 1.6]
sum = 0
highest = 0
#total water intake
for i in water:
    sum += i
    if i > highest:
        highest = i


print(f"Total Water Intake: {sum}")

#average intake
ave = sum / len(water)

print(f"Average water intake: {ave} ")
#highest intake

print(f"Highest intake is {highest}")
