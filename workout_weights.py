weights = [20, 25, 30, 25, 35, 40]
sum = 0
heavy = 0
count  = 0
# total weight lifted
for weight in weights:
    sum += weight
    if weight > heavy:
        heavy = weight
    if weight > 30:
        count += 1

print(f"Total weight lifted: {sum}")
# heaviest weight
print(f"Heaviest weight lifted: {heavy}")
# how many sets above 30
print(f"Number of sets above 30: {count}")