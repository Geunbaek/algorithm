from collections import deque


def convertTimeToMinute(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute


def convertMinuteToTime(minute):
    hour = str(minute // 60).zfill(2)
    minute = str(minute % 60).zfill(2)
    return f"{hour}:{minute}"


def solution(n, t, m, timetable):
    startTime = convertTimeToMinute("09:00")
    timetable = list(map(lambda x: convertTimeToMinute(x), timetable))
    timetable.sort()
    timetable = deque(timetable)
    maxTime = 0
    for i in range(n):
        enterTime = startTime + (i * t)
        curState = []
        while timetable and timetable[0] <= enterTime and len(curState) < m:
            crew = timetable.popleft()
            curState.append(crew)

        if len(curState) < m:
            if curState:
                maxTime = max(maxTime, max(curState), enterTime)
            else:
                maxTime = max(maxTime, enterTime)
        else:
            if len(set(curState)) == 1:
                maxTime = max(maxTime, min(curState) - 1)
            else:
                maxTime = max(maxTime, max(curState) - 1)

    return convertMinuteToTime(maxTime)