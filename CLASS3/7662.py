import sys
input = sys.stdin.readline
import heapq

t = int(input())

for _ in range(t):
    k = int(input())
    min_h = []
    max_h = []
    element_dict = {}
    for _ in range(k):
        oper, num = input().strip().split()
        if oper == 'I':
            heapq.heappush(min_h, int(num))
            heapq.heappush(max_h, -int(num))
            if num not in element_dict:
                element_dict[num] = 1
            else:
                element_dict[num] += 1
        elif oper == "D":
            if element_dict:
                if num == '-1':
                    while min_h and str(min_h[0]) not in element_dict:
                        heapq.heappop(min_h)
                    elem = str(heapq.heappop(min_h))
                    element_dict[elem] -= 1
                    if element_dict[elem] == 0:
                        del element_dict[elem]
                elif num == '1':
                    while max_h and str(-max_h[0]) not in element_dict:
                        heapq.heappop(max_h)
                    elem = str(-heapq.heappop(max_h))
                    element_dict[elem] -= 1
                    if element_dict[elem] == 0:
                        del element_dict[elem]
    if not element_dict:
        print("EMPTY")
    else:
        max_val = -sys.maxsize
        min_val = sys.maxsize
        for key in element_dict.keys():
            if int(key) > max_val:
                max_val = int(key)
            if int(key) < min_val:
                min_val = int(key)
        print(max_val, min_val)
