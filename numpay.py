import numpy as np
arr = np.array([1, 2, 3])
print(arr)
print(arr.ndim)

a = np.array([[[[]]]])
print(a.ndim)
print(a.shape)

range = np.arange(1,10, 2) #start, stop, step
print(range)

arr = np.linspace(0,1,10) #start, stop, number of values
print(arr)

a=np.array([12,13,43,67,6,7,8,9,7])
print(a)
print(a.ndim)
print(a.size)
print(a.shape)

arr = np.logspace(1, 3, 2) #logarithmic scale array -> 10^1 -> 10^3 ... 3 points
print(arr)


# Numpy Data Types and Type Casting
arr=np.array([1,3.0,5.6,4,5])
print(arr)
print(arr.dtype)

arr=np.array([[1,2,3],
            [4,5,6]])
print(arr)
print(arr.ndim)
print(arr.size)
print(arr.shape)
print(arr.itemsize)

#reshape
arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape(2,3)
print(reshaped)

# Arithmetic Operations on Arrays
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b) #adding
print(a/b)
print(b//a)#intger division
print(a*b)


# Universal Function -> ufuncs
arr=np.array([1,4,9,16])
print(np.sqrt(arr))

# Indexing and Slicing

a = [1,2,3,4,5]

a[-1:-4: -1]
a[: :2]


arr = np.array([10,20,30,40,50])
# indexes = 0, 2, 4
print(arr[::2])

# Negative Indexing
print(arr[-1])

# Views vs Copies
arr = np.array([1,2,3,4,5])
view = arr[1:3]
print(view)

# Splitting Arrays:
arr1 = np.array([[1,2], [3,4], [5,6], [7,8]])
print(arr1)

print(np.split(arr1, 4))


# Logical and:
arr=np.array([1, 2, 3])
mask = np.logical_and(arr > 3, arr < 6)
print(mask)

#logical or
arr=np.array([1, 2, 3])
mask = np.logical_or(arr > 3, arr < 6)
print(mask)


#broadcasting
image = np.array([[200, 150], [100, 250]])
print(image.shape)

brightness = image + 50
print(brightness)


#statistical function
c=np.array([10,20,30,38,49,88])
min_c=c.min()
print(min_c)
max_c=c.max()
print(max_c)
sum=min_c+min_c
print(sum)



# array funtion
arr1=np.array([10,11,12,13,14])
arr2=np.array([20,22,12,34,23])
arr3=np.add(arr1,arr2)# same mul,div,diff
print(arr3)

import numpy as np

arr1 = np.array([1, 3])
arr2 = np.array([3, 5])

arr3 = np.dot(arr1, arr2)
print(arr3)
