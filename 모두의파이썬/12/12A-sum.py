def sum_func(n):
    s = 0
    for x in range(1, n+1):
        s = x+s
    return s


print(sum_func(10))
print(sum_func(100))
