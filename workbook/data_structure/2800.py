import sys

input = sys.stdin.readline

def dfs(v, depth, ck):
    if depth == len(positions):
        tmp = ''
        for idx, elem in enumerate(ck):
            if elem == 1:
                tmp += oper[idx]
        results.add(tmp)
        return

    ck[positions[depth][0]], ck[positions[depth][1]] = 1, 1
    v[depth] = 1
    dfs(v, depth + 1, ck)
    ck[positions[depth][0]], ck[positions[depth][1]] = 0, 0
    v[depth] = 0
    dfs(v, depth + 1, ck)

oper = input().strip()
stack = []
positions = []

for index, char in enumerate(oper):
    if char == '(':
        stack.append(index)
    elif char == ')':
        positions.append((stack.pop(), index))

v = [0 for _ in range(len(positions))]
ck = [1 for _ in range(len(oper))]
results = set()

dfs(v, 0, ck)
results = list(results)
results.sort()

for r in results[1:]:
    print(r)