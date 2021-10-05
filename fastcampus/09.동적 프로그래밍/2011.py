import sys
input = sys.stdin.readline

def check(a, b):
    if a == '0': return False
    if a == '1': return True
    if a >= '3': return False
    return b <= '6'

code = input().strip()
dp = [0] * len(code)

if code[0] != '0':
    dp[0] = 1

for i in range(1, len(code)):
    if code[i] != '0':
        dp[i] = dp[i - 1]

    if check(code[i-1], code[i]):
        if i >= 2: dp[i] += dp[i - 2]
        else: dp[i] += 1
        dp[i] %= 1000000

print(dp[-1])

