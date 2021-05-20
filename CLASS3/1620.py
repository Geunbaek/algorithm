import sys
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())
poketmon = defaultdict(int)
poketmon_num = defaultdict(str)

for i in range(1, n+1):
    name = input().strip()
    poketmon[name] = i
    poketmon_num[i] = name

for _ in range(m):
    quiz = input().strip()
    if quiz.isdigit():
        print(poketmon_num[int(quiz)])
    else:
        print(poketmon[quiz])


