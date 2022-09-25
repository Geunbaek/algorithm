def sortFn(arr):
    return [-arr[0]] + [-el for el in arr[1:][::-1]]


def solution(n, info):
    answer = []

    def recur(depth, aScore, lScore, arrow, path):
        if depth >= 11:
            if aScore < lScore:
                answer.append([lScore - aScore] + path)
            return

        aCount = info[depth]
        for lCount in range(arrow + 1):
            if aCount == 0 and lCount == 0:
                recur(depth + 1, aScore, lScore, arrow - lCount, path + [lCount])
                continue

            if aCount >= lCount:
                recur(depth + 1, aScore + 10 - depth, lScore, arrow - lCount, path + [lCount])
            else:
                recur(depth + 1, aScore, lScore + 10 - depth, arrow - lCount, path + [lCount])

    recur(0, 0, 0, n, [])
    if not answer:
        return [-1]

    answer.sort(key=lambda x: sortFn(x))
    return answer[0][1:]
