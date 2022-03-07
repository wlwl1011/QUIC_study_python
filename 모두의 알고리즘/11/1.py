def findAlpa(x):
    length = len(x)

    for i in range(length):
        if i < (length-1)-i:
            if x[i].lower() != x[(length-1)-i].lower():
                return False
    return True


print(findAlpa("Wow"))
