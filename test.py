import numpy as np

def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the entries rowwise for a {rows}x{cols} matrix: ")

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input()))  
        matrix.append(row)

    return np.matrix(matrix)

def print_matrix(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            print(matrix[i, j], end=" ")
        print()

rows1 = int(input("Enter the number of rows for matrix 1: "))
cols1 = int(input("Enter the number of columns for matrix 1: "))

m1 = input_matrix(rows1, cols1)
print("Matrix 1:")
print_matrix(m1)

rows2 = int(input("Enter the number of rows for matrix 2: "))
cols2 = int(input("Enter the number of columns for matrix 2: "))

m2 = input_matrix(rows2, cols2)
print("Matrix 2:")
print_matrix(m2)


if rows1 == rows2:
    if cols1 == cols2:
        sum = m1 + m2
        print("Matrix 1 + Matrix 2:")
        print_matrix(sum)
else:
    print("Matrix dimensions are not compatible for addition.")

if cols1 == rows2:
    det = np.linalg.det(m1)
    print(f"Determinant of Matrix 1: {det}")

    product = m1 * m2
    print("Matrix 1 * Matrix 2:")
    print_matrix(product)
else:
    print("Matrix dimensions are not compatible for multiplication.")

