import sys
input = sys.stdin.readline

n, m = map(int, input().split())
target = sorted(list(map(int, input().split())))

def oper(depth, path):
    if depth >= m:
        for i in path:
            print(target[i], end = ' ')
        print()
        return

    for i in range(n):
        if i not in path:
            oper(depth + 1, path + [i])


oper(0, [])



