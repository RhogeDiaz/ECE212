aList = [1,7,6,3,4,2,8,5,9]

def arrange(list):
    fixedList = []
    i = 0
    while i < len(list) - 1:
        if list[i] > list[i+1]:
            list.append(list[i])
            list.pop(i)
            fixedList.append(i)
            i += 1
        else:
            fixedList.append(i)
            i += 1
    return(fixedList)

print(arrange(aList))
