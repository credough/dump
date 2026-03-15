scores = [10, 15, 7, 20, 18, 12]
#highest score
highest = 0
total =0
count=0
for i in scores:
    if i > highest:
        highest = i
    total += i
    if i >15:
        count += 1

print(f"Highest Score: {highest}")
#total score
print(f"Total Score: {total}")

#how many scores above 15
print(f"Total Scores Above 15:{count}")