pin = "0992"

for i in range(1, 4):
    entered = input("Enter 4 digit PIN:")
    
    if entered == pin:
        print("Matched!")
        break
    else:
        print("Try Again. Attempts left", 3 - i)

print("Done")