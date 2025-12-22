total = 0
count = 0

while True:
    num = input("Enter number (q to quit): ")

    if num == "q":
        break

    total += int(num)
    count += 1

if count > 0:
    print("Average:", total / count)
else:
    print("No numbers entered")
