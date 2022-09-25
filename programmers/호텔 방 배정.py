import sys
sys.setrecursionlimit(10**9)

def solution(k, room_number):
    def find(x):
        if x not in p:
            p[x] = x + 1
            return x
        else:
            p[x] = find(p[x])
            return p[x]

    p = {}
    answer = []
    for num in room_number:
        answer.append(find(num))
    return answer
