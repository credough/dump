def calc(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = int(input("Enter a number:\n"))
print(calc(number))
