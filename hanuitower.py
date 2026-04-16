# Tower of Hanoi

def hanoi(n, start, mid, end):
    if n == 1:
        print(n, ":", start, "->", end)
    else:
        # move n-1 disks from start to mid
        hanoi(n - 1, start, end, mid)

        # move largest disk from start to end
        print(n, ":", start, "->", end)

        # move n-1 disks from mid to end
        hanoi(n - 1, mid, start, end)


def move_count(n):
    if n == 1:
        return 1
    else:
        return 2 * move_count(n - 1) + 1


n = int(input("N > "))

print("총 이동 횟수:", move_count(n))
print("이동 순서:")
hanoi(n, 'A', 'B', 'C')