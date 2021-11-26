import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort(reverse=True)
arr2.sort(reverse=True)
ck = [0 for _ in range(n)]
ck2 = [0 for _ in range(m)]

if arr[0] < arr2[0]:
    print(-1)
else:
    count = m
    time = 0
    while count > 0:
        for i in range(n):
            while ck[i] < m:
                if arr2[ck[i]] <= arr[i] and ck2[ck[i]] == 0:
                    ck2[ck[i]] = 1
                    count -= 1
                    break
                ck[i] += 1
        time += 1

    print(time)






