import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
ans = 0
ans += (v-a) // (a-b)

if (v-a) % (a-b) != 0:
    ans += 1

ans += 1

print(ans)



