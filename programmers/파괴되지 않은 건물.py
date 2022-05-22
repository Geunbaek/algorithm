def solution(board, skill):
    answer = 0
    info_board = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 2:
            info_board[r1][c1] += degree
            info_board[r1][c2 + 1] += -degree
            info_board[r2 + 1][c1] += -degree
            info_board[r2 + 1][c2 + 1] += degree
        else:
            info_board[r1][c1] += -degree
            info_board[r1][c2 + 1] += degree
            info_board[r2 + 1][c1] += degree
            info_board[r2 + 1][c2 + 1] += -degree

    for y in range(len(info_board) - 1):
        for x in range(len(info_board[y]) - 1):
            info_board[y][x + 1] += info_board[y][x]

    for x in range(len(info_board[0]) - 1):
        for y in range(len(info_board) - 1):
            info_board[y + 1][x] += info_board[y][x]

    for y in range(len(board)):
        for x in range(len(board[y])):
            board[y][x] += info_board[y][x]
            if board[y][x] > 0:
                answer += 1

    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])