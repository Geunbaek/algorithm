import sys
input = sys.stdin.readline

def make_time(time):
    time = list(map(int, time.split(":")))
    return time[0] * 60 + time[1]

s, e, q = input().split()
s = make_time(s)
e = make_time(e)
q = make_time(q)
check = {}

while True:
    try:
        time, name = input().split()
        time = make_time(time)
        if time <= s:
            check[name] = False

        if e <= time <= q and name in check:
            check[name] = True

    except:
        break
count = 0
for key, val in check.items():
    if val:
        count += 1
print(count)