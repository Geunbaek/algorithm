from collections import deque


def canCrossBridge(stones, k, diff):
    count = 0

    for stone in stones:
        if stone - diff <= 0:
            count += 1
        else:
            count = 0

        if count >= k:
            return False
    return True


def solution(stones, k):
    left, right = 0, 200_000_000

    while left <= right:
        mid = (left + right) // 2

        if (canCrossBridge(stones, k, mid)):
            left = mid + 1
        else:
            right = mid - 1
    return left