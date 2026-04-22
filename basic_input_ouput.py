sd = 15.00
sw = 25.00

num_sd = int(input("Enter the number of Softdrinks:"))
num_sw = int(input("Enter the number of Sandwhich:"))

total_sd = sd * num_sd 
total_sw = sw * num_sw

print("Total Softdrinks", total_sd)
print("Total Sandwhich", total_sw)

total = total_sd + total_sw
print("Total Amount:", total)

pay = float(input("Enter the amount paid:"))

while total > pay:
    print(f"Insufficient payment. Please pay atleast {total}")
    pay = float(input("Enter the amount paid:"))

print("Payment successful!")
change = pay - total
print(f"Change: {change}")
