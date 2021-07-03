import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(left, right):
    if left == right:
        preorder.append(postorder[right])
        return
    if left > right:
        return

    root = postorder[left]
    for i in range(left+1, right+1):
        if postorder[i] > root:
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
    except:
        break
    else:
        postorder.append(node)


dfs(0, len(postorder)-1)
for e in preorder:
    print(e)
