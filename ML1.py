import numpy as np
arr = np.arange(20,1,-1)
print(arr)

arr2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
min_val = np.amin(arr2D, axis=0)
print("min value is : ",min_val)

arr1 = np.array([0,21,45,89,35,68,45,78])
arr1[arr1 % 2 == 1] = -2
print(arr1)

array1 = np.arange(10).reshape(2,-1)
array2 = np.repeat(1,10).reshape(2,-1)
print(np.concatenate([array1,array2],axis=1))

