numbers = [2,5,9,3,10,12,4]
highest = numbers[0]

for nums in numbers:
    if nums > highest:
        highest = nums

print(highest)