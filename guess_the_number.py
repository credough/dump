import random

def guess_the_num():
 while True:
    secret = random.randint(1,10)
    num = int(input("Enter number you guess (1 - 10):"))

    if num > secret: 
        print("Wrong. Too high. Try again!")
    elif num < secret: 
        print("Wrong. Too low. Try again!")
    else:
        print("Correct!") 
        break

guess_the_num()
   