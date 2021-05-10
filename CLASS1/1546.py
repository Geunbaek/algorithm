import sys

input = sys.stdin.readline

N = int(input())
grade = list(map(int, input().split()))
grade.sort(reverse=True)
max_grade = grade[0]

for idx in range(len(grade)):
    grade[idx] = grade[idx]/max_grade * 100

print(sum(grade)/N)