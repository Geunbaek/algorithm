import sys
input = sys.stdin.readline

s = input().strip()
p = input().strip()
kmp = [0 for _ in range(len(p))]
flag = False

i = 0
j = 1

while j < len(p):
    if p[i] == p[j]:
        kmp[j] = i + 1
        i += 1
        j += 1
    else:
        i = 0
        if p[i] == p[j]:
            kmp[j] = i + 1
            i += 1
            j += 1
        else:
            j += 1

j = 0
for i in range(len(s)):
    while j > 0 and s[i] != p[j]:
        j = kmp[j - 1]
    if s[i] == p[j]:
        if j == len(p) - 1:
            flag = True
            j = kmp[j]
            break
        else:
            j += 1

if flag:
    print(1)
else:
    print(0)




