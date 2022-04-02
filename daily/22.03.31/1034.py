import sys
input = sys.stdin.readline

def arr_to_str(arr):
    return "".join(map(str, arr))

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, list(input().strip()))))

k = int(input())
ans = 0
for y1 in range(n):
    zero_cnt = board[y1].count(0)
    count = 0
    if zero_cnt <= k and zero_cnt % 2 == k % 2:
        for y2 in range(n):
            if arr_to_str(board[y1]) == arr_to_str(board[y2]):
                count += 1
        ans = max(ans, count)
print(ans)