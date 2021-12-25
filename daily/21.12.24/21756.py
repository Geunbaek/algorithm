import sys, copy
input = sys.stdin.readline

n = int(input())
arr = [i+1 for i in range(n)]
arr2 = []

while len(arr) > 1:
    for i, el in enumerate(arr):
        if i % 2 != 0:
            arr2.append(el)
    arr = copy.deepcopy(arr2)
    arr2.clear()
print(arr[0])
