class Heap:
    def __init__(self):
        self.h = [None]

    def push(self, data):
        self.h.append(data)
        now = len(self.h) - 1
        parent = (len(self.h) - 1) // 2
        while now > 1:
            if self.h[now] > self.h[parent]:
                self.h[now], self.h[parent] = self.h[parent], self.h[now]
                now = parent
                parent = now // 2
            else:
                break

    def pop(self):
        if len(self.h) == 1:
            return 0
        max_val = self.h[1]
        self.h[1] = self.h[-1]
        del self.h[-1]
        now = 1
        child_left, child_right = now * 2, now * 2 + 1
        while child_left < len(self.h):

            if child_left < len(self.h) and child_right >= len(self.h):
                if self.h[now] < self.h[child_left]:
                    self.h[now], self.h[child_left] = self.h[child_left], self.h[now]
                    now = child_left
                else:
                    break

            elif child_left < len(self.h) and child_right < len(self.h):
                if self.h[child_left] >= self.h[child_right]:
                    if self.h[now] < self.h[child_left]:
                        self.h[now], self.h[child_left] = self.h[child_left], self.h[now]
                        now = child_left
                    else:
                        break
                elif self.h[child_left] < self.h[child_right]:
                    if self.h[now] < self.h[child_right]:
                        self.h[now], self.h[child_right] = self.h[child_right], self.h[now]
                        now = child_right
                    else:
                        break
            else:
                break

            child_left, child_right = now * 2, now * 2 + 1
        return max_val


import sys
input = sys.stdin.readline

n = int(input())
h = Heap()

for _ in range(n):
    oper = int(input())
    if oper == 0:
        elem = h.pop()
        if elem is None:
            print(0)
        else:
            print(elem)
    else:
        h.push(oper)
"""
13
15
10
8
5
4
20
0
0
0
0
0
0
0
"""