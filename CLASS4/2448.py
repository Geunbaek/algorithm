import sys
input = sys.stdin.readline
import math

star = ["  *   ", " * *  ", "***** "]
def star_func(space):
    for i in range(len(star)):
        star.append(star[i] + star[i])
        star[i] = ("   " * space + star[i] + "   " * space)

N = int(input())
iterate = int(math.log(N//3, 2))

for i in range(iterate):
    star_func(int(pow(2, i)))

for s in star:
    print(s)
