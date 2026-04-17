import numpy as np
arr_2d = np.array([[10,20,30],[40,50,60]])
new_arr =np.insert(arr_2d,1,70,axis=0)
#print(arr_2d)
print(new_arr)
#axis = 0 column wise
#axis = 1 row wise
#axis = none. give in one line