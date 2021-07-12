import sys
from collections import defaultdict
input = sys.stdin.readline

tree = defaultdict(int)
total = 0

while True:
    name = input().strip()
    if not name:
        break
    else:
        tree[name] += 1
        total += 1

for key, val in tree.items():
    tree[key] = "%.4f"%(val / total * 100)

tree = sorted(tree.items())

for n, v in tree:
    print(n, v)

