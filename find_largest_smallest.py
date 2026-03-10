arr = [3,4,2,6,4,5,10]


largest = 0
smallest = 99
sum = 0

for x in arr:
    if x > largest:
        largest = x

    if x < smallest:
        smallest = x
    
    sum += x
    average = sum / 7

print("Largest:", largest)
print("Smallest:", smallest)
print("Average:", average)
