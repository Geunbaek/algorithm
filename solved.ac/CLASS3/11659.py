import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = num_list[start]
        return tree[node]

    mid = (start + end)//2
    tree[node] = init(start, mid, node*2) + init(mid + 1, end, node*2+1)
    return tree[node]

def range_sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return range_sum(start, mid, node*2, left, right) + range_sum(mid+1, end, node*2+1, left, right)

n, m = map(int, input().split())

num_list = list(map(int,input().split()))
tree = [0 for _ in range(3*n)]

init(0, n-1, 1)

for _ in range(m):
    start, end = map(int,input().split())
    print(range_sum(0, n-1, 1, start-1, end-1))
