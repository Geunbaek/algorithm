import sys
input = sys.stdin.readline

def mat_oper(a, b):
    ret = [[0] * len(a) for _ in range(len(a))]
    for y in range(len(a)):
        for x in range(len(a[y])):
            for i in range(len(a)):
                ret[y][x] += a[y][i] * b[i][x]
            ret[y][x] %= 1000000007
    return ret

n= int(input())
if n <= 1:
    print(n)
    exit()

matrix_ans = [[1, 0], [0, 1]]
matrix_a = [[1, 1], [1, 0]]

while n > 0:
    if n % 2 == 1:
        matrix_ans = mat_oper(matrix_ans, matrix_a)
    matrix_a = mat_oper(matrix_a, matrix_a)
    n //= 2

print(matrix_ans[0][1])


