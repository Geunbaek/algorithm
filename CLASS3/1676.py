import math

n = int(input())
factor = math.factorial(n)
cnt =0
while True:
    if factor % 10 == 0:
        factor //= 10
        cnt += 1
    else:
        break

print(cnt)