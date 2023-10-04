import numpy as np

matrix1 = []
print("Enter the entries rowwise: ")

for i in range(3):
    a = []
    for j in range(3):
        a.append(int(input()))
    matrix1.append(a)

for i in range(3):
    for j in range(3):
        print(matrix1[i][j], end=" ")
    print()

m1 = np.matrix(matrix1)
print(m1)

matrix2 = np.array([[6, -1, 0], [0, 1, -2], [3, -8, 1]])
m2 = np.matrix(matrix2)
print(m2)

d = np.linalg.det(m1)
det = int(d)
print(det)

m3 = m1+m2
print(m3)

m4 = m1*m2
print(m4)
