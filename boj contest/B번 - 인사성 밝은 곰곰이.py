import sys
input = sys.stdin.readline

n = int(input())
count = 0
count_set = set()

for _ in range(n):
    string = input().strip()
    if string == "ENTER":
        count += len(count_set)
        count_set = set()
    else:
        count_set.add(string)
count += len(count_set)
print(count)
