import numpy as np
arr = np.array([1,2,np.nan,4,5])
cleaned_arr = np.nan_to_num(arr,nan=7)
print(cleaned_arr)