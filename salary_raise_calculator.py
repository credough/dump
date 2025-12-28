import numpy as np

salaries = np.array([11000,12212,12343,34345])
increase = 0.12

new_salaries = salaries + (salaries * increase)

print("Salary:", salaries)
print("New:", new_salaries)
