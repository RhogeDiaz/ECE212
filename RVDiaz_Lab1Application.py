N = int(input("Enter limit for j: "))
M = int(input("Enter limit for k: "))
j = 1
k = 0

answer = 0
for j in range(1, N + 1):
    for k in range(0, M + 1):
        answer += (j * j) * (k + 1)
print(answer)