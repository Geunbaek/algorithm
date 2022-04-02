import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))
ans = []

def even_check(arr):
    return len(list(filter(lambda x: x % 2 != 0, arr)))

def make_num(arr):
    ret = 0
    for i in range(len(arr)):
        ret += arr[i] * (10 ** (len(arr) - i - 1))
    return ret

def num_to_list(num):
    num = str(num)
    return list(map(int, list(num)))

def recur(arr, path):
    if len(arr) <= 1:
        ans.append(path)
        return
    elif len(arr) == 2:
        next_arr = num_to_list(arr[0] + arr[1])
        recur(next_arr, path + even_check(next_arr))
    else:
        for i in range(1, len(arr)):
            for j in range(i + 1, len(arr)):
                first = make_num(arr[:i])
                second = make_num(arr[i: j])
                third = make_num(arr[j:])
                next_arr = num_to_list(first + second + third)
                recur(next_arr, path + even_check(next_arr))

recur(n, even_check(n))
print(min(ans), max(ans))