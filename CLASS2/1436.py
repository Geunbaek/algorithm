n = int(input())
cnt = 0
for num in range(10000666):
    if str(num).count('666'):
        cnt += 1
    if cnt == n:
        print(num)
        break
