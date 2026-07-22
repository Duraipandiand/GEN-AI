
#1.create a arr=np.arange(1,13) covert into a 3x4 matrix
import numpy as np

arr=np.arange(1,13)
print(arr.reshape(3,4))
print()

#2.Flatten matrix
flat = np.array([[12,13,12],[43,32,32]])
print("before flatten")
print(flat)
print("after flatten")
print(flat.flatten())
print()
#3.multiple every element by 5

arr=np.array([10,20,30,40,50])
print("array element")
print(arr)
print("multiple by 5 each element")
print(arr*5)
print()

#4.Find sum,mean,median,maximum,minumum and standard deviation

arr=np.array([10, 20, 30, 40, 50, 60 ])
print("Original array")
print(arr)
print("SUM of array")
print(arr.sum())
print("MEAN of array")
print(arr.mean())
print("MEDIAN of array")
print(np.median(arr))
print("MAXIMUM of array")
print(arr.max())
print("MINIMUM of array")
print(arr.min())
print("STANDARD DEVIATION of array")
print(arr.std())

#create two 2x2 matrix and perform addition,element wise mutliplication and matrix multiplication.

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Matrix A")
print(a)

print("Matrix B")
print(b)

print("Addition")
print(a + b)

print("Element-wise Multiplication")
print(a * b)

print("Matrix Multiplication")
print(a @ b)