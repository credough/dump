import numpy as np

random_scores = np.random.randint(61,100, size = 30)

print("Scores:", random_scores)
print("Average:", np.mean(random_scores))
print("Highest:", np.max(random_scores))
print("Lowest:", np.min(random_scores))
print("Median:", np.median(random_scores))