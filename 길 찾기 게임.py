import sys

sys.setrecursionlimit(10 ** 9)


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def makeTree(nodeinfo, node, index, minX, maxX):
    x = node.data[1]
    y = node.data[2]
    left, right = None, None
    start = index

    for i in range(index, len(nodeinfo)):
        if nodeinfo[i][2] < y:
            y = nodeinfo[i][2]
            start = i
            break

    for i in range(start, len(nodeinfo)):
        if nodeinfo[i][2] == y:
            if minX < nodeinfo[i][1] < maxX and nodeinfo[i][1] < x:
                left = [nodeinfo[i], i]
            elif minX < nodeinfo[i][1] < maxX and nodeinfo[i][1] > x:
                right = [nodeinfo[i], i]
        else:
            break

    if left:
        node.left = TreeNode(left[0])
        makeTree(nodeinfo, node.left, left[1], minX, x)
    if right:
        node.right = TreeNode(right[0])
        makeTree(nodeinfo, node.right, right[1], x, maxX)

    return node


def preorder(node):
    if node:
        ret = []
        ret.append(node.data[0])

        if node.left:
            ret += preorder(node.left)

        if node.right:
            ret += preorder(node.right)
        return ret


def postorder(node):
    if node:
        ret = []

        if node.left:
            ret += postorder(node.left)

        if node.right:
            ret += postorder(node.right)

        ret.append(node.data[0])
        return ret


def solution(nodeinfo):
    nodeinfo = [[i + 1, node[0], node[1]] for i, node in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: (-x[2], -x[1]))

    root = TreeNode(nodeinfo[0])

    tree = makeTree(nodeinfo, root, 0, -1, 100001)

    return [preorder(tree), postorder(tree)]
