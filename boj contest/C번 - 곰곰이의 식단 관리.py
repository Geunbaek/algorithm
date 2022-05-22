import math
import sys
input = sys.stdin.readline

n = int(input())
string = input().strip()

count = string.count('C')
print(math.ceil(count / (n - count + 1)) if count != n else n)