import sys
input = sys.stdin.readline

while True:
    length = list(map(int, input().split()))
    if length == [0, 0, 0]:
        break
    length.sort()
    if length[0] ** 2 + length[1] ** 2 == length[2] ** 2:
        print("right")
    else:
        print("wrong")