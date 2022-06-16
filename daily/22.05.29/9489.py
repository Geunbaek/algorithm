import sys
input = sys.stdin.readline
from collections import deque, defaultdict

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    arr = list(map(int, input().split()))
    tree = defaultdict(list)
    group = [[arr[0]]]

    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == 1:
            group[-1].append(arr[i])
        else:
            group.append([arr[i]])

    q = deque(group)
    q2 = deque(group[1:])

    depth = 0
    tree[depth] = [group[0]]
    depth += 1
    while q2:
        el = q.popleft()
        for _ in range(len(el)):
            if not q2:
                break
            tree[depth].append(q2.popleft())
        depth += 1

    for key, val in tree.items():
        check = -1
        for i, l in enumerate(val):
            if k in l:
                check = i
                break
        if check == -1:
            continue
        else:
            count = 0
            for i, l in enumerate(val):
                if i == check:
                    continue
                else:
                    count += len(l)
    print(count)





