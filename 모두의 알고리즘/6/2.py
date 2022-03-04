def findStudent(numArr, nameArr, num):
    length = len(numArr)
    for i in range(length):
        if numArr[i] == num:
            return nameArr[i]
    return '(?)'


stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]
print(findStudent(stu_no, stu_name, 14))
