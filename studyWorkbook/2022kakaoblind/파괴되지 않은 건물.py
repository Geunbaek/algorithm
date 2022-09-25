def solution(board, skill):
    answer = 0
    damageBoard = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        sign = 1 if type == 1 else -1
        damageBoard[r1][c1] += -sign * degree
        damageBoard[r2 + 1][c1] += sign * degree
        damageBoard[r1][c2 + 1] += sign * degree
        damageBoard[r2 + 1][c2 + 1] += -sign * degree

    for y in range(len(damageBoard) - 1):
        for x in range(len(damageBoard[y]) - 1):
            damageBoard[y][x + 1] += damageBoard[y][x]

    for x in range(len(damageBoard[0]) - 1):
        for y in range(len(damageBoard) - 1):
            damageBoard[y + 1][x] += damageBoard[y][x]

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] + damageBoard[y][x] > 0:
                answer += 1

    return answer