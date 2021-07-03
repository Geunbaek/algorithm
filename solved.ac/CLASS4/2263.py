import sys
input = sys.stdin.readline
results = []
sys.setrecursionlimit(10**8)

def sol(in_left, in_right, post_left, post_right):
    if post_left > post_right or in_left > in_right:
        return
    root = postorder[post_right]
    results.append(root)
    p = position[root]
    left = p - in_left

    sol(in_left, p-1, post_left, post_left+ left-1)
    sol(p+1, in_right, post_left+left, post_right-1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = {}
for i in range(n):
    position[inorder[i]] = i

sol(0, n-1, 0, n-1)
for r in results:
    print(r, end = ' ')


