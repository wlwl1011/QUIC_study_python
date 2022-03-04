
def findIdx(arr, num):
    length = len(arr)

    result = []
    for i in range(length):
        if arr[i] == num:
            result.append(i)

    return result


arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(findIdx(arr1, 1))
