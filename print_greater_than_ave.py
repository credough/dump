import numpy as np

scores = np.array([54,67,4,2,12,34,65,76])

print(np.mean(scores))

for i in range(0,8):
    if(scores[i] > np.mean(scores)):
     print(scores[i])