import numpy as np

value = np.array([2,3,4,5,6])
print(value*3)

newvalue = [x*3 for x in value]
print(newvalue)

res = [2,3,4,5,6]
print(res*3)