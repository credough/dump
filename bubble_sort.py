arr = [1,4,3,8,2,6]

n = 6

for i in range(6):
  for j in range(6 - i - 1):
    if(arr[j] > arr[j+1]):
     temp = 0
     temp = arr[j]
     arr[j] = arr[j+1]
     arr[j+1] = temp
    

for i in range(6):
   print("arr[",i,"] =", arr[i] )