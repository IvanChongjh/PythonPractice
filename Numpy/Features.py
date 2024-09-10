import numpy as np

# utilising .ndim to gather the dimension of declared array 
# 0D array
arr1 = np.array(25)
# 1D array
arr2 = np.array([1,2,3])
# 2D array 
arr3 = np.array([[1,2,3],[4,5,6]])
# 3d array 
arr4 =np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)
print(arr4)