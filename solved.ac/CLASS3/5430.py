import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    arr = list(map(int, input().strip().replace("[", "").replace(']', "").replace(",", ' ').split()))
    arr = deque(arr)
    ck = False
    is_reversed = False
    for char in p:
        if char == 'R':
            if is_reversed:
                is_reversed = False
            else:
                is_reversed = True
        elif char == "D":
            if not arr:
                ck = True
                break
            if is_reversed:
                arr.pop()
            else:
                arr.popleft()
    if ck:
        print('error')
    else:
        if not arr:
            print('[]')
        elif is_reversed:
            arr.reverse()
            ans = "["
            for idx in range(len(arr)-1):
                ans += str(arr[idx]) + ","
            ans += str(arr[-1]) + "]"
            print(ans)
        else:
            ans = "["
            for idx in range(len(arr) - 1):
                ans += str(arr[idx]) + ","
            ans += str(arr[-1]) + "]"
            print(ans)
