import random


def make_question():
    a = random.randint(1, 30)
    b = random.randint(1, 30)

    userInput = input("Please input number (+ : 1, - : 2, * : 3)")

    if int(userInput) == 1:
        print(a, "+", b, "=")
        temp = a+b
        return temp
    if int(userInput) == 2:
        print(a, "-", b, "=")
        temp = a-b
        return temp
    if int(userInput) == 3:
        print(a, "*", b, "=")
        temp = a*b
        return temp


sc1 = 0
sc2 = 0

for x in range(5):
    compare = make_question()
    temp = input()
    if compare == int(temp):
        sc1 = sc1+1
    else:
        sc2 = sc2+1

print("you're score is ", sc1, "in five times.")
