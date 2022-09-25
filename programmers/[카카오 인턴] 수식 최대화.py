from itertools import permutations
from collections import deque
import copy


def seperateNumAndOperator(expression):
    tempNum = ""
    nums = deque()
    operators = deque()
    for char in expression:
        if char.isdigit():
            tempNum += char
        else:
            operators.append(char)
            nums.append(int(tempNum))
            tempNum = ""
    nums.append(int(tempNum))
    return [nums, operators]


def getCalculatedNum(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    else:
        return num1 * num2


def calculateOfSpecificOperator(operator, nums, operators):
    newNums = deque([nums.popleft()])
    newOperators = deque()

    while operators:
        o = operators.popleft()
        if o == operator:
            newNums[-1] = getCalculatedNum(o, newNums[-1], nums.popleft())
        else:
            newNums.append(nums.popleft())
            newOperators.append(o)
    return [newNums, newOperators]


def solution(expression):
    nums, operators = seperateNumAndOperator(expression)
    answer = 0
    for ops in permutations(["+", "-", "*"], 3):
        result = 0
        copyNums, copyOperators = copy.copy(nums), copy.copy(operators)
        for op in ops:
            copyNums, copyOperators = calculateOfSpecificOperator(op, copyNums, copyOperators)
        answer = max(answer, abs(copyNums[0]))
    return answer