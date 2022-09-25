def solution(board, moves):
    answer = 0
    r, c = len(board), len(board[0])
    newBoard = []
    for x in range(c):
        newBoard.append([])
        for y in range(r - 1, -1, -1):
            if board[y][x] != 0:
                newBoard[-1].append(board[y][x])

    basket = []

    for move in moves:
        if newBoard[move - 1]:
            doll = newBoard[move - 1].pop()
            if basket and basket[-1] == doll:
                basket.pop()
                answer += 2
            else:
                basket.append(doll)

    return answer