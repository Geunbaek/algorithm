from collections import deque


def solution(queue1, queue2):
    length = (len(queue1) + len(queue2)) * 2
    q1 = deque(queue1)
    q2 = deque(queue2)

    left = sum(queue1)
    right = sum(queue2)
    count = 0

    while count < length:
        while left < right and count < length:
            number = q2.popleft()
            left += number
            right -= number
            q1.append(number)
            count += 1

        while left > right and count < length:
            number = q1.popleft()
            left -= number
            right += number
            q2.append(number)
            count += 1

        if left == right:
            return count
    return -1