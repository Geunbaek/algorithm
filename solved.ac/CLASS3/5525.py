import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()
target = "I" + "OI" * n
cnt = 0
ans = 0
i = 0

while i <= m - 3:
    if s[i] == "I" and s[i+1] == "O" and s[i+2] == "I":
        cnt += 1
        i += 2
    else:
        cnt = 0
        i += 1

    if cnt == n:
        cnt -= 1
        ans += 1


print(ans)

"""
3
13
OOIOIOIOIIOII
"""