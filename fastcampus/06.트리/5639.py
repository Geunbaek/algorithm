import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def dfs(left, right):
    if left == right:
        postorder.append(preorder[left])
        return
    elif left > right:
        return

    root = preorder[left]

    for i in range(left + 1, right + 1):
        if preorder[i] > root:
            dfs(left + 1, i-1)
            dfs(i, right)
            dfs(left, left)
            break
    else:
        dfs(left + 1, right)
        dfs(left, left)


postorder = []
preorder = []
while True:
    try:
        node = int(input())
        preorder.append(node)
    except:
        break

dfs(0, len(preorder) - 1)
for n in postorder:
    print(n)

