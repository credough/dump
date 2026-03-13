attendance = {
    "Day 1": {"Alice": True, "Bob": False, "Charlie": True},
    "Day 2": {"Alice": True, "Bob": False}
}

days = ("Day 1", "Day 2")
names = ("Alice", "Bob", "Charlie")
alice = 0
bob = 0
charlie = 0
# Accessing attendance[day][name]
# Exercise 1: Print all students who were present on Day1

print("Students who were present on Day 1:")

for name in names:
 if attendance["Day 1"][name] == True:
  print(name)

# Exercise 2: Count total days each students attended

for day in days:
   if attendance[day]["Alice"] == True:
    alice += 1
   if attendance[day]["Bob"] == True:
    bob += 1
   
if attendance["Day 1"]["Charlie"] == True:
    charlie += 1

print("Days Alice attended:\n", alice)
print("Days Bob attended:\n", bob)
print("Days Charlie attended:\n", charlie)



"""
for da in day:
     for nam in names:
         print(f"{attendance[da]}")
         """