# Python program for Fibonacci Series

fibo = [1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
iteration = abs(int(input("Enter the number of iterations: ")))
First_Val = abs(int(input("Enter the first value: ")))
i = 2

for x in range(len(fibo)):
    if First_Val == fibo[x]:
        Second_Val = First_Val + fibo[x-1]
        print(First_Val)
        print(Second_Val)

        while i < iteration:
            Next = First_Val + Second_Val
            First_Val = Second_Val
            Second_Val = Next
            i += 1
            print(Next)

