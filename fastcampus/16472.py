import sys
input = sys.stdin.readline

n = int(input())

string = input().strip()

cnt = [0] * 26
kind = 0
ans = 0
l = 0

for r in range(len(string)):
    cnt[ord(string[r]) - ord('a')] += 1
    if cnt[ord(string[r]) - ord('a')] == 1:
        kind += 1

    while kind > n:
        cnt[ord(string[l]) - ord('a')] -= 1
        if cnt[ord(string[l]) - ord('a')] == 0:
            kind -= 1
        l += 1
    ans = max(ans, r - l + 1)

print(ans)

