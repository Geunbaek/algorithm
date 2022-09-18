import sys, copy

input = sys.stdin.readline

def getWinner(first, second, firstState, secondState):
    if info[firstState][secondState] == 2:
        return first
    elif info[firstState][secondState] == 1:
        return first if first > second else second
    else:
        return second

def getNextPlayer(turn):
    for i in range(3):
        if i not in turn:
            return i
    return -1

def dfs(turn, now, depth, winCount, roundCount):
    global answer
    if depth >= n + 1:
        return

    first = turn[0]
    second = turn[1]

    state = [now - 1, p1[roundCount[1]] - 1, p2[roundCount[2]] - 1]
    winner = getWinner(first, second, state[first], state[second])

    newWinCount = copy.deepcopy(winCount)
    newWinCount[winner] += 1

    if newWinCount[winner] >= k:
        if winner == 0:
            answer = True
        return

    nextPlayer = getNextPlayer(turn)

    newRoundCount = copy.deepcopy(roundCount)
    newRoundCount[first] += 1
    newRoundCount[second] += 1

    if nextPlayer != 0:
        for i in range(1, n + 1):
            if visited[i] == 0:
                visited[i] = 1
                dfs([winner, nextPlayer], i, depth + 1, newWinCount, newRoundCount)
                visited[i] = 0
    else:
        dfs([winner, nextPlayer], now, depth + 1, newWinCount, newRoundCount)

n, k = map(int, input().split())
answer = False
info = []

for _ in range(n):
    info.append(list(map(int, input().split())))

p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
visited = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    visited[i] = 1
    dfs([0, 1], i, 0, [0, 0, 0], [0, 0, 0])
    visited[i] = 0

if answer:
    print(1)
else:
    print(0)