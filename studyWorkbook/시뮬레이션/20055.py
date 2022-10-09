import sys
input = sys.stdin.readline
from collections import deque

class Robot:
    def __init__(self, index):
        self.index = index

    def move(self):
        global count

        if self.index == q1[-1]:
            return False

        nextIndex = (self.index + 1) % (2 * n)

        if robots and robots[-1]:
            if robots[-1].index == nextIndex:
                return True

        if arr[nextIndex] > 0:
            self.index = nextIndex
            arr[nextIndex] -= 1
            if arr[nextIndex] == 0:
                count += 1
        return True

    def __repr__(self):
        return f"{self.index}"

n, k = map(int, input().split())
arr = list(map(int, input().split()))

q1 = deque([i for i in range(n)])
q2 = deque([2 * n - i - 1 for i in range(n)])

count = 0
turn = 0
robots = deque()

while count < k:
    down = q1.pop()
    up = q2.popleft()

    if robots and robots[0].index == down:
        robots.popleft()

    q1.appendleft(up)
    q2.append(down)

    length = len(robots)
    for _ in range(length):
        robot = robots.popleft()
        if robot.move():
           robots.append(robot)

    if arr[q1[0]] > 0:
        robots.append(Robot(q1[0]))
        arr[q1[0]] -= 1
        if arr[q1[0]] == 0:
            count += 1

    turn += 1
print(turn)


