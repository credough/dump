scores = [85, 90, 78, 92, 88, 76]

sum = 0
highest = 0
count = 0

# average score
for score in scores:
    sum += score

ave = sum / len(scores)

print(f"Average score: {ave}")

# highest score
for score in scores:
    if score > highest:
        highest = score
    if score >= 80:
        count += 1

print(f"Highest score: {highest}")

# how many students passed (>= 80)
print(f"The number of students passed: {count}")
