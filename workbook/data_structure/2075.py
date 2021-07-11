import sys
input = sys.stdin.readline

n = int(input())
ans = sorted(list(map(int, input().split())), reverse= True)[:n]

for _ in range(n-1):
    ck = sorted(list(map(int, input().split())), reverse= True)[:n]
    ans_index, ck_index = 0, 0
    temp = []
    while len(temp) < n:
        if ans[ans_index] > ck[ck_index]:
            temp.append(ans[ans_index])
            ans_index += 1
        else:
            temp.append(ck[ck_index])
            ck_index += 1
    ans = temp[:]
print(ans[-1])
