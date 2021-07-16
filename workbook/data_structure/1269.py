import sys

input = sys.stdin.readline

n, m = map(int, input().split())

n_arr = set(map(int, input().split()))
m_arr = set(map(int, input().split()))

ans = len(n_arr - m_arr) + len(m_arr - n_arr)
print(ans)