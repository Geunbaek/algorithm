import math

def getKDecimalNumber(n, k):
    kDecimalNumber = ""
    while n >= k:
        kDecimalNumber += str(n % k)
        n //= k
    kDecimalNumber += str(n)
    return kDecimalNumber[::-1]

def isPrimeNumber(num):

    if num == 1:
        return False
    if num == 2:
        return True

    for i in range(3, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    kDecimalNumber = getKDecimalNumber(n, k)
    numbers = list(map(int, filter(lambda x: x, kDecimalNumber.split("0"))))

    for num in numbers:
        if isPrimeNumber(num):
            answer += 1
    return answer

assert solution(437674, 3) == 3
assert solution(110011, 10) == 2