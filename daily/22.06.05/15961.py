import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
race = []

for _ in range(n):
    rice = int(input())
    race.append(rice)

race.extend(race[:k])
now = {}
total = 0
ans = 0

for index, r in enumerate(race):
    total += 1
    now[r] = now.get(r, 0) + 1
    if total >= k:
        if c in now:
            ans = max(ans, len(now))
        else:
            ans = max(ans, len(now) + 1)

        now[race[index - k + 1]] -= 1

        if now[race[index - k + 1]] == 0:
            del now[race[index - k + 1]]

        total -= 1


print(ans)






