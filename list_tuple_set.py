""" fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits.insert(1, "kiwi")
fruits.remove("banana")
for x in fruits:
    print(x)
"""
"""
colors = ("red", "green", "blue")

for x in colors:
    print(x)

my_list = list(colors)
my_list.append("yellow")
my_list.remove("red")

for x in my_list:
    print(x)
"""
"""
num = {1, 2, 3, 4, 5}
num.add(6)
num.remove(2)
print(num)
"""

my_dict = {
    "name": "Aaron",
    "age": 21
}

my_dict["age"] = 22
my_dict["course"] = "CS"
print(my_dict["age"])
print(my_dict["name"])
print(my_dict["course"])

my_dict.pop("age")
print(my_dict)