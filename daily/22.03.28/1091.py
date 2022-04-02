import sys
input = sys.stdin.readline

def arr_to_string(arr):
    return "".join(map(str, arr))

def check(arr):
    for i in range(0, len(arr), 3):
        if arr[i] == 0 and arr[i + 1] == 1 and arr[i + 2] == 2:
            continue
        else:
            return False
    return True

n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
visit = set()
visit.add(arr_to_string(p))
count = 0
if check(p):
    print(0)
    exit()

while True:
    temp = [0 for _ in range(len(p))]
    for i, num in enumerate(s):
        temp[num] = p[i]
    string = arr_to_string(temp)
    if string in visit:
        print(-1)
        break

    p = temp
    count += 1

    if check(temp):
        print(count)
        break




