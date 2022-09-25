from collections import deque, defaultdict


def solution(gems):
    gemCount = len(set(gems))

    gemsCounter = defaultdict(int)
    q = deque()
    dist = len(gems)
    answer = [0, len(gems) - 1]

    for i, gem in enumerate(gems):
        gemsCounter[gem] += 1
        q.append([i, gem])
        while len(gemsCounter) == gemCount and gemsCounter[q[0][1]] > 1:
            firstGemIndex, firstGem = q.popleft()
            gemsCounter[firstGem] -= 1
        if len(gemsCounter) == gemCount and len(q) >= gemCount and abs(q[-1][0] - q[0][0]) < dist:
            dist = abs(q[-1][0] - q[0][0])
            answer = [q[0][0] + 1, q[-1][0] + 1]

    return answer


