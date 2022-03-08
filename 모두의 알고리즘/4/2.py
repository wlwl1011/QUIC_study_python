def findMax(idx, max):
    
    a = [2, 1, 4, 7, 0]
    lenth = len(a)
    if(idx <= 0):
        return max
    if a[idx-1] > max:
        max = a[idx]

    return findMax(idx-1, max)


print(findMax(5, 0))
