import sys, copy
from itertools import permutations
from collections import defaultdict

input = sys.stdin.readline

def deepcopy(matrix):
    ret = []
    for z in range(2):
        ret.append([])
        for y in range(5):
            ret[-1].append([])
            for x in range(5):
                ret[-1][-1].append(matrix[z][y][x])

    return ret



def getQuality(kiln):
    qualityDic = defaultdict(int)

    for y in range(5):
        for x in range(5):
            qualityDic[kiln[1][y][x]] += kiln[0][y][x]
    return qualityDic['R'] * 7 + qualityDic['B'] * 5 + qualityDic['G'] * 3 + qualityDic['Y'] * 2


def recur(depth, kiln, order):
    global answer
    if depth >= 3:
        answer = max(answer, getQuality(kiln))
        return

    for y in range(5):
        for x in range(5):
            if not isValidRange(x, y):
                continue
            for i in range(4):
                materialInfo = materialDict[order[depth]][i]
                newKiln = deepcopy(kiln)
                putMaterials(newKiln, materialInfo['materials'], materialInfo['materialsInfo'], x, y)
                recur(depth + 1, newKiln, order)


def isValidRange(x, y):
    return 0 <= x <= 1 and 0 <= y <= 1

def rotate(matrix):
    rotatedMatrix = []
    for x in range(4):
        rotatedMatrix.append([])
        for y in range(3, -1, -1):
            rotatedMatrix[-1].append(matrix[y][x])

    return rotatedMatrix

def putMaterials(kiln, materials, materialsInfo, sx, sy):
    for y in range(sy, sy + 4):
        for x in range(sx, sx + 4):
            newQuality = kiln[0][y][x] + materials[y - sy][x - sx]
            if newQuality < 0:
                kiln[0][y][x] = 0
            elif newQuality > 9:
                kiln[0][y][x] = 9
            else:
                kiln[0][y][x] = newQuality

            if materialsInfo[y - sy][x - sx] == "W":
                continue
            else:
                kiln[1][y][x] = materialsInfo[y - sy][x - sx]


n = int(input())
materialDict = {}

for i in range(n):
    materials = []
    materialsInfo = []

    for _ in range(4):
        materials.append(list(map(int, input().split())))

    for _ in range(4):
         materialsInfo.append(list(input().split()))


    materialDict[i] = [{
        "materials": materials,
        "materialsInfo": materialsInfo
    }]

    for _ in range(3):
        materials = rotate(materials)
        materialsInfo = rotate(materialsInfo)
        materialDict[i].append({
            "materials": materials,
            "materialsInfo": materialsInfo
        })

case = [i for i in range(n)]
answer = 0
for comb in permutations(case, 3):
    kiln = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(2)]
    recur(0, kiln, comb)

print(answer)







