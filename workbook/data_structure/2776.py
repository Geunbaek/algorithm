import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    n_arr = set(map(int, input().split()))

    m = int(input())
    m_arr = list(map(int, input().split()))
    for m_elem in m_arr:
        if m_elem in n_arr:
            print(1)
        else:
            print(0)
