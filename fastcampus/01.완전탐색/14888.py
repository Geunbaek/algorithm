import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
oper = list(map(int, input().strip().split()))

def rec(n, depth, result):
    if depth == len(arr):
        result.append(n)
        return

    for i in range(len(oper)):
        if oper[i] != 0:
            oper[i] -= 1
            if i == 0:
                new_n = n + arr[depth]
            elif i == 1:
                new_n = n - arr[depth]
            elif i == 2:
                new_n = n * arr[depth]
            elif i == 3:
                if n < 0:
                    new_n = -n // arr[depth]
                    new_n = -new_n
                else:
                    new_n = n // arr[depth]
            rec(new_n, depth + 1, result)
            oper[i] += 1

result = []
rec(arr[0], 1, result)
result.sort()

print(result[-1])
print(result[0])
