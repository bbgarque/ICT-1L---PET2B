import numpy as np

# creating matrices
# Initials: BBG [2, 2, 7]
# Second letters: EEA [5, 5, 1]

matrix_1 = np.array([[2, 2, 7], [5, 5, 1]])
print("Matrix 1:\n", matrix_1)

# Student number first 3 numbers: 202 [2, 0, 2]
# Student number last 3 numbers: 459 [4, 5, 9]

matrix_2 = np.array([[2, 0, 2], [4, 5, 9]])
print("\nMatrix 2:\n", matrix_2)

# Matrix Addition
matrix_3 = matrix_1 + matrix_2
print("\nMatrix 3 (Addition):\n", matrix_3)

# Scalar Multiplication
matrix_4 = matrix_1 * 2
print("\nMatrix 4 (Scalar Multiplication):\n", matrix_4)

# Matrix Transpose
matrix_5 = matrix_2.T
print("\nMatrix 5 (Transpose of Matrix 2):\n", matrix_5)

# Matrix Multiplication
matrix_6 = np.dot(matrix_3, matrix_5)
print("\nMatrix 6 (Matrix Multiplication):\n", matrix_6)

# Sum of all elements in Matrix 3
sum_matrix_3 = np.sum(matrix_3)
print("\nSum of all elements in Matrix 3:", sum_matrix_3)

# Zero Matrix
matrix_7 = np.zeros((2, 3))
print("\nMatrix 7 (Zero Matrix):\n", matrix_7)
