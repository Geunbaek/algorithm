def match(a, b):
    if len(a) != len(b):
        return False

    for char1, char2 in zip(a, b):
        if char1 == "*" or char2 == "*":
            continue
        if char1 != char2:
            return False
    return True


def solution(user_id, banned_id):
    def dfs(depth, path):
        nonlocal answer
        if depth >= len(matchCounter):
            if path not in answer:
                answer.append(path)
            return

        for el in matchCounter[depth]:
            if el not in path:
                dfs(depth + 1, path | {el})

    matchCounter = [[] for _ in range(len(banned_id))]
    answer = []

    for i, bid in enumerate(banned_id):
        for uid in user_id:
            if match(bid, uid):
                matchCounter[i].append(uid)
    for el in matchCounter[0]:
        dfs(1, {el})

    return len(answer)