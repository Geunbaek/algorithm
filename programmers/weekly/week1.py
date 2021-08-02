def solution(price, money, count):
    answer = [price*i for i in range(1, count+1)]
    return sum(answer) - money if (sum(answer) - money) > 0 else 0