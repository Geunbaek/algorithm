import sys
input = sys.stdin.readline

def mul_matrix(a, b):
    ret = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            val = 0
            for k in range(n):
                val += a[y][k] * b[k][x]
            ret[y][x] = val % 1000
    return ret

def recur(m, cnt):
    if cnt == 1:
        return m

    elif cnt % 2 == 0:
        ret = recur(m, cnt//2)
        return mul_matrix(ret, ret)
    else:
        ret = recur(m, cnt - 1)
        return mul_matrix(m, ret)

n, b = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

ans = recur(matrix, b)

for y in range(n):
    for x in range(n):
        print(ans[y][x] % 1000, end=' ')
    print()
