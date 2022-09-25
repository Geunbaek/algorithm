def getDist(start, end):
    x, y = start
    nx, ny = end

    return abs(nx - x) + abs(ny - y)


def solution(numbers, hand):
    answer = ''
    keypad = {
        1: [0, 0], 2: [1, 0], 3: [2, 0],
        4: [0, 1], 5: [1, 1], 6: [2, 1],
        7: [0, 2], 8: [1, 2], 9: [2, 2],
        "*": [0, 3], 0: [1, 3], "#": [2, 3],
    }

    left = keypad["*"]
    right = keypad["#"]
    for number in numbers:
        if number in (1, 4, 7):
            answer += "L"
            left = keypad[number]
        elif number in (3, 6, 9):
            answer += "R"
            right = keypad[number]
        else:
            leftDiff = getDist(left, keypad[number])
            rightDiff = getDist(right, keypad[number])
            if leftDiff < rightDiff:
                left = keypad[number]
                answer += 'L'
            elif leftDiff > rightDiff:
                right = keypad[number]
                answer += 'R'
            else:
                if hand == 'left':
                    left = keypad[number]
                    answer += 'L'
                else:
                    right = keypad[number]
                    answer += 'R'

    return answer