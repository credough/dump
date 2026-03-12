classList = []
passed = []
failed = []

print("Please enter Student NAME with its corresponding GRADE")

name = ""
val = ""
count = 0
passed_c = 0
failed_c = 0

while True:
    name = str(input("Enter name:"))

    try: 
      grade = float(input("Enter grade for {name}:"))
      classList.append((name,grade))
      count += 1
      if grade < 3.0:
         passed.append((name, grade))
         passed_c +=1
      else:
         failed.append((name,grade))
         failed_c += 1

      val = input("Enter More? [Y/N]")
      if val == "N" or val == "n":
        break


    except ValueError:
       print("Invalid grade. Please enter a number")

classList.sort()

print("Class List:", classList)
print("Total Number of Students:", count)
print("Passed Students:", passed)
print("Total Number of PASSED Students:", passed_c)
print("Failed Students:", failed)
print("Total Number of FAILED Students:", failed_c)
