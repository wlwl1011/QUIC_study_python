def matingFunc(input):
    lenth = len(input)
    for i in range(0, lenth-1):
        for j in range(i+1, lenth):
            print(input[i], '-', input[j])


name = ["Tom", "Jerry", "Mike"]
matingFunc(name)
