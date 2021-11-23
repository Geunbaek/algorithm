import sys
input = sys.stdin.readline

n = int(input())
cut = set()
ans = []

for _ in range(n):
    string = input().strip()
    strings = string.split()
    target = -1
    total = 0
    for idx, s in enumerate(strings):
        if s[0].lower() not in cut:
            cut.add(s[0].lower())
            target = total
            break
        total += len(s) + 1
    if target != -1:
        temp = ""
        for idx, char in enumerate(string):
            if idx != target:
                temp += char
            else:
                temp += f'[{char}]'
        ans.append(temp)
    else:
        temp = ''
        ck = True
        for idx, char in enumerate(string):
            if char.strip() and char.lower() not in cut and ck:
                cut.add(char.lower())
                target = idx
                temp += f'[{char}]'
                ck= False
            else:
                temp += char
        ans.append(temp)
for el in ans:
    print(el)

