import numpy as np
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([100,200,300,400])
new_arr = np.concatenate((arr1,arr2))
print(new_arr)