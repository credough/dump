sales = [1200, 1500, 800, 2000, 1700]
total = 0
count=0
highest=0
#total sales
for i in sales:
    total += i
    if i > highest:
        highest = i
    if i > 1500:
        count += 1

print(f"Total Sales: {total}")
#highest sale

print(f"Highest Sale: {highest}")
#how many sales above 1500

print(f"Sales above 1500: {count}")

#average sale
ave = total / len(sales)

print(f"Average sale: {ave}")
