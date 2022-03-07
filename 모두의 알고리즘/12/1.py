def findStudent(a):
    dic = {39: "Justin", 14: "John", 67: "Mike", 105: "Summer"}
    if a in dic:
        return dic[a]
    else:
        return "?"


print(findStudent(39))
print(findStudent(9))
