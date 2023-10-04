import numpy as np


# Function to input a matrix of given dimensions
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the entries rowwise for a {rows}x{cols} matrix: ")

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input()))  # Allow decimal inputs
        matrix.append(row)

    return np.matrix(matrix)


# Function to print a matrix
def print_matrix(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            print(matrix[i, j], end=" ")
        print()


# Input matrix1 dimensions
rows1 = int(input("Enter the number of rows for matrix 1: "))
cols1 = int(input("Enter the number of columns for matrix 1: "))

# Input matrix1
matrix1 = input_matrix(rows1, cols1)
print("Matrix1:")
print_matrix(matrix1)

# Input matrix2 dimensions
rows2 = int(input("Enter the number of rows for matrix 2: "))
cols2 = int(input("Enter the number of columns for matrix 2: "))

# Input matrix2
matrix2 = input_matrix(rows2, cols2)
print("Matrix2:")
print_matrix(matrix2)

# Perform operations if dimensions are compatible
if cols1 == rows2:
    # Calculate determinant of matrix1
    det = np.linalg.det(matrix1)
    print(f"Determinant of matrix1: {det}")

    # Add matrices
    result_add = matrix1 + matrix2
    print("Matrix1 + Matrix2:")
    print_matrix(result_add)

    # Multiply matrices
    result_mult = matrix1 * matrix2
    print("Matrix1 * Matrix2:")
    print_matrix(result_mult)
else:
    print("Matrix dimensions are not compatible for multiplication.")


# We define two functions, input_matrix and print_matrix, to handle user input and printing matrices.
# The user is prompted to enter the dimensions for both matrix1 and matrix2.
# The input_matrix function is used to input the values for both matrices.
# The code checks if the dimensions of matrix1 and matrix2 are compatible for matrix multiplication (the number of columns in matrix1 must equal the number of rows in matrix2).
# If the dimensions are compatible, it calculates the determinant of matrix1, adds the matrices, and multiplies the matrices.
# The results are printed to the console.
# This code allows the user to input any n by m dimensional array for both matrices and performs the specified operations as long as the dimensions are compatible.