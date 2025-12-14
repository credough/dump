password = input("Enter Password:")

if len(password) < 8:
    print("Weak password")
elif password.isalpha() or password.isdigit():
    print("Medium")
else:
    print("Strong password")