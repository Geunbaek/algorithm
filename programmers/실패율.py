def solution(N, stages):
    stages.sort()
    userCount = len(stages)
    fails = [[i, 0] for i in range(N + 1)]
    for i in range(1, N + 1):
        solvedCount = stages.count(i)
        if userCount:
            fails[i][1] = solvedCount / userCount
        else:
            fails[i][1] = 0
        userCount -= solvedCount
    answer = list(map(lambda x: x[0], sorted(fails[1:], key = lambda x: (-x[1], x[0]))))
    return answer