score = 0

while True:
    print("1. Add score")
    print("2. Show score")
    print("3. Exit")

    choice = input("Enter choice:")

    if choice == "1":
        score += 1
        print("Score added")
    elif choice == "2":
        print("Score:", score)
    elif choice == "3":
        break
    else:
        print("Invalid input")
