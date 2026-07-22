
#1.Create a 1-D array containing 5,10,15,20,25.
print("#1.Create a 1-D array containing 5,10,15,20,25.")
import numpy as np
arr=np.array([5,10,15,20,25])

print(arr)
print()

#Create a 3x3 matrix filled with zeros and ones
print("#2.Create a 3x3 matrix filled with zeros and ones")

arr1=np.zeros([3,3,3])
print(arr1)
print()

#ones

arr2=np.ones([3,3,3])
print(arr2)
print()


#3.Create a 4x4 Indentity Matrix
print("#3.Create a 4x4 Indentity Matrix")

indetity=np.eye(4)
print(indetity)
print()




#4.Create Numbers from 10 to 50 with the step of 5.

print("#4.Create Numbers from 10 to 50 with the step of 5.")

step=np.arange(10,50,5)
print(step)
print()

#5.Create 8 equally spaced numbers between 0 and 1

print("#5.Create 8 equally spaced numbers between 0 and 1")

spaced=np.linspace(0,1,8)
print(spaced)
print()

######
#Array Indexing and slicing

#1.Create a arr=np.array([5,10,15,20,25,30]).print first element,last element and third element.

print("#1.Create a arr=np.array([5,10,15,20,25,30]).print first element,last element and third element.")

ar=np.array([5,10,15,20,25,30])
print(f"First element: {ar[0]} Last element : {ar[-1]} Third element: {ar[2]}")
print()

#2.print 10 15 20 using slicing

print("#2.print 10 15 20 using slicing")
ar1=np.array([5,10,15,20,25,30])
print(ar1[1:4])

#Reverse the array
print("Reverse the array")
ar2=np.array([5,10,15,20,25,30])
print(ar[::-1])

#print only even position element
print("#print only even position element")
even=np.array([5,10,15,20,25,30])
print(even[1::2])

#Create marks=np.array([45,78,90,32,88,67]).print only marks greater than 70.

print("#Create marks=np.array([45,78,90,32,88,67]).print only marks greater than 70.")
marks=np.array([45,78,90,32,88,67])
res=[]

for i in marks:
    if i > 70:
        res.append(i)
print(res)

print()
print(marks[marks > 70])


