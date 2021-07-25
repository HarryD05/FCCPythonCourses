# Importing libraries
import numpy

### Array creation ###
print("1 - Create a numpy array of size 10, filled with zeros.")
array1 = numpy.array([0] * 10)
print(array1)
array1 = numpy.zeros(10)
print(array1)

print("\n2 - Create a numpy array with values ranging from 10 to 49.")
array2 = numpy.arange(10, 50)
print(array2)

print("\n3 - Create a numpy matrix of 2*2 integers, filled with ones.")
matrix3 = numpy.ones((2, 2), dtype=numpy.int8)
print(matrix3)

print("\n4 - Create a numpy matrix of 3*2 float numbers, filled with ones.")
matrix4 = numpy.ones((3, 2), dtype=numpy.float16)
print(matrix4)

print("\n5 - Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones.")
X = numpy.arange(4, dtype=numpy.int8)
array5 = numpy.ones_like(X)
print(array5)

print("\n6 - Create a numpy matrix of 4*4 integers, filled with fives.")
matrix6 = numpy.ones((4, 4), dtype=numpy.int8) * 5
print(matrix6)

print("\n7 - Create a numpy array, filled with 3 random integer values between 1 and 10.")
array7 = numpy.random.randint(10, size=3)
print(array7)

print("\n8 - Create a 3*3*3 numpy matrix, filled with random float values.")
matrix8 = numpy.random.random((3, 3, 3))
print(matrix8)

print("\n9 - Create a numpy array with the odd numbers between 1 to 10.")
array9 = numpy.arange(1, 11, step=2)
print(array9)

print("\n10 - Create a numpy array with numbers from 1 to 10, in descending order.")
array10 = numpy.arange(10, 0, step=-1)  # My solution
print(array10)
array10 = numpy.arange(1, 11)[::-1]  # Given solution
print(array10)

print("\n11 - Create a 3*3 numpy matrix, filled with values ranging from 0 to 8.")
matrix11 = numpy.arange(9).reshape((3, 3))
print(matrix11)


### Array manipulation ###
print("\n12 - Reverse the given numpy array (first element becomes last).")
X = numpy.array([-5, -3, 0, 10, 40])
array12 = X[::-1]
print(array12)

print("\n13 - Order (sort) the given numpy array.")
X = numpy.array([0, 10, -5, 40, -3])
X.sort()
print(X)

print("\n14 - Given the X numpy matrix, change the last row with all 1.")
X = numpy.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
X[3] = 1  # Use X[-1] to always do last row
print(X)


### Boolean arrays (masks) ###
print("\n15 - Given the X numpy array, make a mask showing negative elements.")
X = numpy.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
mask15 = X < 0
print(mask15)

print("\n16 - Given the X numpy array, get numbers higher than 5.")
X = numpy.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
array16 = X[X > 5]
print(array16)

print("\n17 - Given the X numpy array, get numbers equal to 2 or 10.")
X = numpy.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
array17 = X[(X == 2) | (X == 10)]
print(array17)


### Summary statistics ###
print("\n18 - Given the X numpy matrix, show the sum of its columns.")
X = numpy.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
array18 = X.sum(axis=0)
print(array18)

print("\n19 - Given the X numpy matrix, show the mean value of its rows.")
X = numpy.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
array19 = X.mean(axis=1)
print(array19)

print("\n20 - Given the X numpy array, show the max value of its elements.")
X = numpy.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10])
maxNum = X.max()
print(maxNum)
