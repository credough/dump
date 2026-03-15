hours = [2,3,1,4,2,5]
sum = 0
count = 0
#total hours
for hr in hours:
    sum += hr
    if hr > 3:
        count += 1

print(f"Total Hours: {sum}")
#average hours
ave = sum / len(hours)

print(f"Average Hours: {ave}")
#days above 3 hours
print(f"Days above 3 hours: {count}")


