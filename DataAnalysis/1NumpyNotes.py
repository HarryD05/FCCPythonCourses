# Importing libraries
import numpy


### Basic structures in numpy ###
print("Basic structures")

# Basic numpy arrays - uses less memory, can specify type
array1 = numpy.array([1, 2, 3, 4], dtype=numpy.int8)  # dtype is int8
array2 = numpy.array([0, 0.5, 1, 1.5, 2])  # dtype is float64

# Matrices - each row has to have same number of columns
matrix1 = numpy.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix1.shape)  # Rows and columns of matrix
print(matrix1.ndim)  # Number of dimensions
print(matrix1.size)  # Total count of elements in matrix
print(matrix1[1])  # Second row
print(matrix1[1, 0])  # First element of second row
print(matrix1[:, :2])  # Can slice like normal python arrays
# All rows but first 2 columns of each row


### Random matrices ###
print("\nRandom matrices")

# 3 x 3 matrices with elements between 0 and 100
randomMatrix = numpy.random.randint(100, size=(3, 3))
print(randomMatrix)

# Summary statistics ### (all work for arrays and matrices)
print("\nSummary statistics")

print(array1.sum())  # Sum of all elements
print(array1.mean())  # Mean of all elements
print(array1.std())  # Standard deviation of all elements
print(array1.var())  # Variance of all elements
print(matrix1.sum(axis=0))  # Returns array with sums of each column
print(matrix1.sum(axis=1))  # Returns array with sums of each row


### Broadcasting and vectorised operations ###
print("\nBroadcasting and vectorised operations")

array3 = numpy.arange(4)  # Creating an array from 0 to n (numpy.arange(n))
array3 += 10  # Adds 10 to every item in array
array3 *= 10  # Multiplies every item in array by 10
print(array3)

array4 = numpy.arange(4)
array5 = numpy.array([10, 10, 10, 10])
print(array4 + array5)  # Only works if both arrays are same size
print(array4 * array5)


### Boolean arrays ###
print("\nBoolean arrays")

array6 = numpy.arange(4)

# You can use an array of booleans to select certain elements
print(array6[[True, False, False, True]])

# You can get whether or not each elements meets a condition
# (returns boolean array)
print(array6 >= 2)

# You can specify conditions for which elements display
print(array6[array6 >= 2])

# You can combine functions eg
# All elements greater than or equal to mean
print(array6[array6 >= array6.mean()])

# All elements not greater than or equal to mean
print(array6[~(array6 >= array6.mean())])

# Can use | to represent OR, & to represent AND
# If you use boolean condition to filter a matrix an array of true elements is returned


### Linear Algebra ###
print("\nLinear algebra")

# Defining 2 matrices
matrix2 = numpy.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix3 = numpy.array([
    [6, 5],
    [4, 3],
    [2, 1]
])

# Dot product
print(matrix2.dot(matrix3))
print(matrix2 @ matrix3)

# Transpose matrix
print(matrix3.T)
