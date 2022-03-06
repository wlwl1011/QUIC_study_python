def binary_search(a, x, start, end):

    mid = (start + end)//2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search(a, x, mid+1, end)
    else:
        return binary_search(a, x, mid, end-1)
    return -1


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36, 0, len(d)))
print(binary_search(d, 50, 0, len(d)))
