import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ox = input().strip()
    score = 0
    point = 1

    for char in ox:
        if char == "O":
            score += point
            point += 1
        else:
            point = 1

    print(score)