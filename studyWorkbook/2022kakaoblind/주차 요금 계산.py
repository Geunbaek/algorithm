import math
from collections import defaultdict

def getMinuteFromTime(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute

def solution(fees, records):
    basicMinute, basicFee, extraMinuteUnit, extraFee = fees
    answer = defaultdict(int)
    park = {}
    costs = []

    for record in records:
        time, carId, state = record.split()
        minute = getMinuteFromTime(time)
        if state == "IN":
            park[carId] = minute
        else:
            enterTime = park[carId]
            timeOfUse = minute - enterTime
            answer[carId] += timeOfUse
            del park[carId]

    for carId, enterTime in park.items():
        minute = getMinuteFromTime("23:59")
        timeOfUse = minute - enterTime
        answer[carId] += timeOfUse


    for carId, timeOfTotalUse in answer.items():
        if timeOfTotalUse <= basicMinute:
            cost = basicFee
        else:
            cost = basicFee + math.ceil((timeOfTotalUse - basicMinute) / extraMinuteUnit) * extraFee
        costs.append((carId, cost))
    return list(map(lambda x: x[1], sorted(costs, key = lambda x: int(x[0]))))


print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))