import sys
input = sys.stdin.readline

n = list(input().strip())
m = int(input())
now = 100
cnt = abs(now - int("".join(n)))

broken_button = set(list(map(int, input().split())))
for i in range(1000000):
    i = list(str(i))
    count = 0
    ck = False
    for num in i:
        if int(num) in broken_button:
            ck = True
            break
        count += 1
    if ck:
        continue
    if int("".join(n)) == int("".join(i)):
        cnt = min(cnt, count)
        continue
    if not ck:
        count += abs(int("".join(n))-int("".join(i)))
        # print(i,count)
        cnt = min(cnt, count)

print(cnt)




