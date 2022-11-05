import sys
input = sys.stdin.readline

def isValidRange(x, y):
    return 0 <= x < n and 0 <= y < n

def getPositionsInfo(favoriteStudents):
    posInfo = []
    for y in range(n):
        for x in range(n):
            if classRoom[y][x] != 0:
                continue

            emptyRoomCount = 0
            favoriteStudentCount = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not isValidRange(nx, ny):
                    continue
                if classRoom[ny][nx] in favoriteStudents:
                    favoriteStudentCount += 1
                elif classRoom[ny][nx] == 0:
                    emptyRoomCount += 1
            posInfo.append((favoriteStudentCount, emptyRoomCount, y ,x))
    return posInfo

def getTotalSatisfaction():
    result = 0
    for y in range(n):
        for x in range(n):
            favoriteStudentCount = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not isValidRange(nx, ny):
                    continue
                if classRoom[ny][nx] in relationship[classRoom[y][x]]:
                    favoriteStudentCount += 1
            result += getSatisfaction(favoriteStudentCount)
    return result

def getSatisfaction(favoriteStudentCount):
    if favoriteStudentCount == 0:
        return 0
    elif favoriteStudentCount == 1:
        return 1
    elif favoriteStudentCount == 2:
        return 10
    elif favoriteStudentCount == 3:
        return 100
    else:
        return 1000

n = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

classRoom = [[0 for _ in range(n)] for _ in range(n)]
relationship = [[] for _ in range(n ** 2 + 1)]

for _ in range(n ** 2):
    studentNumbers = list(map(int, input().split()))
    posInfo = getPositionsInfo(studentNumbers[1:])
    posInfo.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    target = posInfo[0]
    classRoom[target[2]][target[3]] = studentNumbers[0]
    relationship[studentNumbers[0]].extend(studentNumbers[1:])

print(getTotalSatisfaction())