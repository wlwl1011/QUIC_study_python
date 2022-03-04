# 패턴 : 위에 걸 목적지가 아닌 곳으로, 아래걸 목적지로 옮겨야 한다.
def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return

    hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos, "->", to_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos)


print("n=1")
hanoi(1, 1, 3, 2)
