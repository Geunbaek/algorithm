import sys
input = sys.stdin.readline
import math

n = int(input())
result = 4

for i in range(int(math.sqrt(n)), int(math.sqrt(n//2))-1, -1):
    num = n - i*i
    if num == 0:
        result = min(result, 1)
        break
    for j in range(int(math.sqrt(num)), int(math.sqrt(num//2))-1, -1):
        num2 = num - j*j
        if num2 == 0:
            result = min(result, 2)
            break
        for k in range(int(math.sqrt(num2)), int(math.sqrt(num2//2))-1, -1):
            num3 = num2 - k*k
            if num3 == 0:
                result = min(result, 3)
                break

print(result)



