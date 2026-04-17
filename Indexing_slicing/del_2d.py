import numpy as np
arr1 = np.array([[10,20],[40,50]])
new_arr2d =np.delete(arr1,1,axis=0)
# axis = o --> remove row
# axis = 1 -->remove column
# obj -->1 means remove element from index =1

print(arr1)
print(new_arr2d)