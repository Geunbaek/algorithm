from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    foodCounter = defaultdict(int)
    foodNameInfo = {}
    answer = []
    for order in orders:
        for i in range(2, len(order) + 1):
            for food in combinations(sorted(list(order)), i):
                foodName = "".join(food)
                foodCounter[foodName] += 1
                if len(food) in foodNameInfo:
                    foodNameInfo[len(food)] = max(foodNameInfo[len(food)], foodCounter[foodName])
                else:
                    foodNameInfo[len(food)] = foodCounter[foodName]
    for c in course:
        for key, val in foodCounter.items():
            if len(key) == c and val >= 2 and val == foodNameInfo[c]:
                answer.append(key)

    answer.sort()
    return answer