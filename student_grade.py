grades = []
highest = 0
lowest = 0
failed = 0
passed = 0
total = 0

count = int(input("How many subjects?"))

for i in range(count):
    grades = int(input("Grade:\n"))

    total += grades

    if highest is None or grades > highest:
        highest = grades 

    if grades is None or grades < highest:
        lowest = grades

    if grades >= 75:
        passed += 1
    else:
        failed += 1

average = total / count

print("\n Highest grade", highest)
print("Lowest grade:", lowest)
print("Failed:", failed)
print("Passed:", passed)
print("Average:", average)

    
