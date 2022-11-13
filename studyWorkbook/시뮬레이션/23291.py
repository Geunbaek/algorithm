import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = deque([deque(map(int, input().split()))])

def check(x, y):
    print(arr)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    now = arr[y][x]
    result = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0:
            continue
        try:
            _next = arr[ny][nx]
            if _next > now:
                result += (_next - now) // 5
            else:
                result -= (now - _next) // 5
        except:
            continue
    return result

def rotate():
    _min = min(arr[-1])

    for i in range(len(arr[-1])):
        if arr[-1][i] == _min:
            arr[-1][i] += 1

    last = arr[-1].popleft()
    arr.appendleft(deque([last]))

    while True:
        if len(arr[-1]) - len(arr[-2]) < len(arr):
            break

        temp = deque()

        for x in range(len(arr[-2])):
            temp.append(deque())
            for y in range(len(arr) - 1, -1, -1):
                temp[-1].append(arr[y].popleft())

        while len(arr) > 1:
            arr.popleft()
        while temp:
            arr.appendleft(temp.pop())

    ret = deque()
    for x in range(len(arr[-1])):
        for y in range(len(arr) -1, -1, -1):
            try:
                ret.append(arr[y][x] + check(x, y))
            except:
                break
    return ret

def rotate2():
    arr.appendleft(deque())
    for _ in range(len(arr[-1]) // 2):
        arr[-2].appendleft(arr[-1].popleft())

    # while len(arr[-1]) != 2:




arr = deque([rotate()])
print(rotate2())





