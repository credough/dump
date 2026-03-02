#for(int i = 0; i < 10; i++)

#answer = 'y'
#while answer == 'y':
 
nilagay = int(input("Input:"))
for x in range(1,nilagay + 1):
      for y in range(1,x + 1):
         print(y,end='')
      print(" ")
      
for x in range(nilagay-1, 0, -1):
      for y in range(1,x+1):
         print(y,end='')
      print(" ")  

#answer = str(input("Continue?")).lower()
   
  

