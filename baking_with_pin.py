correct_pin = "1234"
attempts = 3
balance = 1000

while attempts > 0:
    pin = input("Enter pin: ")

    if pin == correct_pin:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Account Locked")

else:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice")

        if choice == "1":
            print("Balance remaining:", balance)
        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            if amount >= 0:
                balance += amount
            elif amount < 0:
                print("Invalid input")
        elif choice == "3":
            amount = int(input("Enter amount to withdraw"))
            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful. Balance left:", balance)
            elif amount > balance:
                print("Invalid amount")
        elif choice == "4":
            print("Thank you!")

        else: 
            print("Invalid choice")

