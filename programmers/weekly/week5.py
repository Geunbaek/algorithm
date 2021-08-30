import sys

sys.setrecursionlimit(10 ** 8)


def rec(arr, result, results, depth):
    if depth == 5:
        if result != '' and result not in results:
            results.append(result)
        return

    for el in arr:
        rec(arr, result + el, results, depth + 1)


def solution(word):
    results = []
    arr = ['A', 'E', 'I', 'O', 'U', '']
    rec(arr, '', results, 0)
    results.sort()
    # print(results)
    return results.index(word) + 1