import sys
input = sys.stdin.readline
from collections import defaultdict

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reversed_graph = [[] for _ in range(n + 1)]
degree = [0 for _ in range(n + 1)]
now = defaultdict(int)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    reversed_graph[y].append(x)
    degree[y] += 1

for _ in range(k):
    oper, building = map(int, input().split())
    if oper == 1:
        if degree[building] == 0:
            now[building] += 1
            for el in graph[building]:
                if degree[el] > 0:
                    degree[el] -= 1
        else:
            print("Lier!")
            break
    else:
        if now[building] == 0:
            print("Lier!")
            break
        else:
            now[building] -= 1
            if now[building] == 0:
                # for el in reversed_graph[building]:
                #     degree[el] += 1
                for el in graph[building]:
                    degree[el] += 1

else:
    print('King-God-Emperor')