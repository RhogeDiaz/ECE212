# Function to input a matrix of given dimensions
def store_matrix(rows, cols):
    matrix = []
    print(f"Enter the entries rowwise for a {rows}x{cols} matrix: ")

    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            row.append(float(input()))  # Allow decimal inputs
        matrix.append(row)

    return matrix

# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

# Input matrix1 dimensions
rows1 = int(input("Enter the number of rows for matrix 1: "))
cols1 = int(input("Enter the number of columns for matrix 1: "))

# Input matrix1
matrix1 = store_matrix(rows1, cols1)
print("Matrix1:")
print_matrix(matrix1)

# Input matrix2 dimensions
rows2 = int(input("Enter the number of rows for matrix 2: "))
cols2 = int(input("Enter the number of columns for matrix 2: "))

# Input matrix2
matrix2 = store_matrix(rows2, cols2)
print("Matrix2:")
print_matrix(matrix2)

# Perform operations if dimensions are compatible
if cols1 == rows2:
    # Calculate determinant of matrix1
    def determinant(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            det = 0
            for i in range(len(matrix)):
                cofactor = [row[:i] + row[i+1:] for row in matrix[1:]]
                det += matrix[0][i] * determinant(cofactor) * (-1) ** i
            return det

    det = determinant(matrix1)
    print(f"Determinant of matrix1: {det}")

    # Add matrices
    if rows1==rows2:
        if cols1==cols2:
            result_add = []
            for i in range(0, rows1):
                row = []
                for j in range(0, cols1):
                    row.append(matrix1[i][j] + matrix2[i][j])
                result_add.append(row)
            
            print("Matrix1 + Matrix2:")
            print_matrix(result_add)
    else:
        print("Matrix dimensions are not compatible for addition.")
        
    # Multiply matrices
    result_mult = []
    for i in range(0, rows1):
        row = []
        for j in range(0, cols2):
            element = 0
            for k in range(0, cols1):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result_mult.append(row)
    
    print("Matrix1 * Matrix2:")
    print_matrix(result_mult)
else:
    print("Matrix dimensions are not compatible for multiplication.")
