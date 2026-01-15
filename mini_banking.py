balance = 0

while True:
    print("\n1. Deposit")
    print("\n2. Withdraw")
    print("\n3. Check Balance")
    print("\n4. Exit")

    choice = input("choose option:")

    if choice == "1":
        amount = int(input("enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Deposited successfully")
        else:
            print("Invalid")

    elif choice == "2":
        amount = int(input("Enter amount to withdraw:"))
        if amount > balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("invalid withdrawal. enter again.")
        else:
            balance -= amount
            print("Successful withdrawal")

    elif choice == "3":
        print("Your remaining balance:", balance)

    elif choice == "4":
        print("Thank you!")
        break

    else: 
        print("invalid option")

