import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    height, width, num = map(int, input().split())
    front = str((num-1) % height + 1)
    back = str((num-1)//height + 1)
    if len(back) == 1:
        back = "0" + back
    print(front + back)
