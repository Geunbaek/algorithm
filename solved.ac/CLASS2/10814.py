import sys
input = sys.stdin.readline

n = int(input())
name_arr = []

for idx in range(n):
    age, name = input().strip().split()
    name_arr.append((int(age), name, idx))

name_arr.sort(key = lambda x:(x[0], x[2]))
for age, name, _ in name_arr:
    print(age, name)
