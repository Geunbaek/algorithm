import sys
input = sys.stdin.readline

n = int(input())
elem = set()

for _ in range(n):
    op = input().strip().split()
    if len(op) == 1:
        if op[0] == 'all':
            for i in range(1, 21):
                if i not in elem:
                    elem.add(i)
        elif op[0] == 'empty':
            elem = set()
    else:
        op[1] = int(op[1])
        if op[0] == 'add':
            if op[1] not in elem:
                elem.add(op[1])
        elif op[0] == 'remove':
            if op[1] in elem:
                elem.remove(op[1])
        elif op[0] == 'check':
            if op[1] in elem:
                print(1)
            else:
                print(0)
        elif op[0] == 'toggle':
            if op[1] in elem:
                elem.remove(op[1])
            else:
                elem.add(op[1])