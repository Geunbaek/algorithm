n = int(input())
cnt = 0
for i in range(1, n+1):
    i = str(i)
    if len(i) == 1:
        cnt += 1
        continue
    diff = int(i[0]) - int(i[1])
    for j in range(1, len(i)):
        if int(i[j-1]) - int(i[j]) != diff:
            break
    else:
        cnt += 1
print(cnt)
