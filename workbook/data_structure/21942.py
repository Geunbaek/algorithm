import sys
from collections import defaultdict
input = sys.stdin.readline

months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

n, l, f = map(str, input().strip().split())
l = l.split('/')
hours, mins = l[1].split(":")
total_mins = int(l[0]) * 1440 + int(hours) * 60 + int(mins)
ans = defaultdict(int)

current = defaultdict(dict)

for _ in range(int(n)):
    date, t, item, name = map(str, input().strip().split())

    if item not in current[name]:
        current[name][item] = (date, t)
    else:
        start = current[name][item][0].split('-')
        end = date.split('-')

        total = 0
        total_min = 0

        start_month = int(start[1])
        start_date = int(start[2])
        end_month = int(end[1])
        end_date = int(end[2])

        start_hour = int(current[name][item][1].split(':')[0])
        start_min = int(current[name][item][1].split(':')[1])
        end_hour = int(t.split(':')[0])
        end_min = int(t.split(':')[1])

        total_min += (end_hour - start_hour) * 60 + (end_min - start_min)

        if start_month != end_month:
            total += months[start_month] - start_date
            start_month += 1

            while start_month < end_month:
                total += months[start_month]
                start_month += 1

            total += end_date
        else:
            total += end_date - start_date


        total_min += total * 1440

        del current[name][item]

        if total_mins < total_min:
            ans[name] += (total_min - total_mins) * int(f)

if ans:
    ans = sorted(ans.items(), key = lambda x:x[0])
    for name, cost in ans:
        print(name, cost)
else:
    print(-1)
