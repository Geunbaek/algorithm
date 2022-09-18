import sys

input = sys.stdin.readline

c = int(input())

for _ in range(c):
    line = list(map(int, input().split()))
    n, scores = line[0], line[1:]
    avg = sum(scores) / n
    count = 0

    for score in scores:
        if score > avg:
            count += 1

    answer = round((count / n * 100), 3)
    print("%0.3f" % answer + "%")