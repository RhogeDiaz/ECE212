#Rhoge Vhir A. Diaz
#ECE 2A

import math

m = int(input("Enter the value for outer loop end point m: "))
n = int(input("Enter the value for inn er loop end point n: "))
u = int(input("Enter the value for the outer loop starting point j: "))
v = int(input("Enter the value for the inner loop starting point k: "))

def doubleSum(m, n, u, v):
    totalSum = 0
    for j in range(u, m+1):
        for k in range(v, n+1):
            totalSum += math.sqrt(abs(j - k))

    return(int(totalSum))

if __name__ == "__main__":
    print("The final answer is:", doubleSum(m, n, u, v))