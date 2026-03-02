
n = int(input("How many?"))

sum = 0
odd = 0
even = 0
sum_even = 0
num_nega = 0
num_pos = 0
sum_odd = 0
bet = 0

for i in range(1, n+1):
  num = int(input("Enter Numbers{i}:"))

  sum += num

  if num > 0:
     num_pos += 1
  else:
    num_nega += 1

  if num % 2 == 0:
    sum_even += num
    even += 1
  else: 
    odd += 1
    sum_odd += num


  if num >= 50 and num <= 100:
    bet += 1


print("Sum:", sum)
print("Num of even", even)
print("Num of odd", odd)
print("sum of even", sum_even)
print("Sum of odd", sum_odd)
print("Num of negative", num_nega)
print("Num of positive", num_pos)
print("Nums between 50 to 100", bet)