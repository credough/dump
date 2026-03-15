sleep = [6, 7, 5,8,7,8]
lowest = 99
#average sleep
sum = 0
count=0
for i in sleep:
    sum += i
    if i < lowest:
      lowest = i
    if i < 6:
       count += 1

ave = sum / len(sleep)
print(f"Average: {ave}")
#lowest sleep
print(f"Lowest: {lowest}")

#how many days below 6 hours
print(f"Number of days below 6: {count}")
