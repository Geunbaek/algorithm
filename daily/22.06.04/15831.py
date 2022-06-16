import sys
input = sys.stdin.readline

n, b, w = map(int, input().split())
string = input().strip()

l, r = 0, 0
b_cnt, w_cnt = 0, 0
ans = 0

while r < n:
    if b_cnt > b:
        if string[l] == 'W':
            w_cnt -= 1
        else:
            b_cnt -= 1
        l += 1

    else:
        if string[r] == "W":
            w_cnt += 1
        else:
            b_cnt += 1
        r += 1

    if w_cnt >= w and b_cnt <= b:
        ans = max(ans, r - l)

print(ans)