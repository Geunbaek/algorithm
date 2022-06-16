import sys
input = sys.stdin.readline

def check():
    cnt = 0
    for i in (0, 3, 6):
        target = path[i]
        if target == '.':
            continue

        for j in (i + 1, i + 2):
            if path[j] != target:
                break
        else:
            cnt += 1

    for i in (0, 1, 2):
        target = path[i]
        if target == '.':
            continue

        for j in (i + 3, i + 6):
            if path[j] != target:
                break
        else:
            cnt += 1

    if path[0] != '.':
        if path[0] == path[4] and path[0] == path[8]:
            cnt += 1

    if path[2] != ".":
        if path[2] == path[4] and path[2] == path[6]:
            cnt += 1

    if cnt:
        return True

    return False



def oper(depth):
    if depth >= 9:
        ans.add("".join(path))
        return

    if check():
        ans.add("".join(path))
        return

    for i in range(9):
        if path[i] == ".":
            path[i] = 'X' if depth % 2 == 0 else "O"
            oper(depth + 1)
            path[i] = "."

path = ["." for _ in range(9)]
ans = set()
oper(0)

while True:
    string = input().strip()
    if string == "end":
        break

    if string in ans:
        print("valid")
    else:
        print("invalid")



