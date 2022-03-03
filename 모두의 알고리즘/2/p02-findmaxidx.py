
def findMax(a):
    num = len(a)
    max = 0
    maxidx = 0
    for x in range(num):
        if max < a[x]:
            max = a[x]
            maxidx = x

    return x


a = [1, 2, 3, 4, 5, 6]
print(findMax(a))
