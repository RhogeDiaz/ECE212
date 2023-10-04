i = 0
First_Val = 0
Second_Val = 1

while i < 10:
    if i <= 1:
        Next = i
    else:
        Next = First_Val + Second_Val
        First_Val = Second_Val
        Second_Val = Next
        print(Next)
    i = i + 1