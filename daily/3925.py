import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    line = list(map(lambda x: int(x, 16), input().strip().split()))
    while len(line) < 9:
        line += list(map(lambda x: int(x, 16), input().strip().split()))

    n9 = line.pop()
    k = 0
    mask = 1
    while mask < 2 ** 32:
        _sum = 0
        for d in line:
            _sum += d

        if (n9 ^ _sum) & mask:
            k |= mask
            n9 ^= mask
            for i in range(8):
                line[i] ^= mask

        mask <<= 1
    print(hex(k)[2:])

