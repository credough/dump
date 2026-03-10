stringggs = "Ang ingay ng unggoy"

count = 0

for x in stringggs.lower():
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        count += 1

print("Num of vowels:", count)
