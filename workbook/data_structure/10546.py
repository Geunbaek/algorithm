import sys

input = sys.stdin.readline

n = int(input())
participant = []
complete = []

for _ in range(n):
    participant.append(input().strip())

for _ in range(n-1):
    complete.append(input().strip())

participant.sort()
complete.sort()

for p, c in zip(participant, complete):
    if p != c:
        print(p)
        break
else:
    print(participant[-1])