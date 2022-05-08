import numpy as np

print(np.__version__)
arr1 = np.array([1,2,3,4,5])
arr2 = np.array((1,2,3,4,5))
print(arr1)
print(arr1.ndim)
print(arr2)
print(type(arr1))
print(type(arr2))
arr3 = np.array([9,8,7,6], ndmin = 5)
print(arr3)
print(arr3.ndim)
print(arr3.dtype)
arr4 = np.array([9.6,88.2,7,6.3])
arr5 = arr4.astype('i')
arr5 = arr4.astype(int)
print(arr4)
print(arr4.dtype)
print(arr5)
print(arr5.dtype)
print(arr5.shape)
arr6 = arr5.reshape(4,-1)
print(arr6)
for i in arr6:
    print(i)
for i in np.nditer(arr6):
    print(i)
print(arr6.shape)
arr7 = arr6.reshape(-1)
print(arr7)

# A CODE BY TUSHAR SINGH