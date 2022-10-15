import sys, copy
from collections import deque
input = sys.stdin.readline

def getOperResult(a, b, oper):
    if oper == '+':
        return a[0] + b[0]
    elif oper == '*':
        return a[0] * b[0]
    elif oper == '-':
        return a[0] - b[0]

def getOpersResult(nums, opers):
    nums = deque(nums)
    opers = deque(opers)

    while opers:
        first, second = nums.popleft(), nums.popleft()
        oper = opers.popleft()
        nums.appendleft([getOperResult(first, second, oper), 0])
    return nums[0][0]

def recur(nowNums, nowOpers):
    for i in range(len(nowOpers)):
        if nowNums[i][1] == 0 and nowNums[i + 1][1] == 0:
            newNums = copy.deepcopy(nowNums)
            newOpers = copy.deepcopy(nowOpers)
            newNums[i] = [getOperResult(newNums[i], newNums.pop(i + 1), newOpers.pop(i)), 1]
            recur(newNums, newOpers)
    results.append(getOpersResult(nowNums, nowOpers))

results = []
n = int(input())
expression = list(input().strip())
if n == 1:
    print(expression[0])
    exit()

numbers = []
operators = []

for char in expression:
    if char.isdigit():
        numbers.append([int(char), 0])
    else:
        operators.append(char)

recur(numbers, operators)
print(max(results))

