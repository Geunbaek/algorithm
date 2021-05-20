import sys
input = sys.stdin.readline

x = input().split('-')
sum1 = 0
for i in x[0].split('+'):
    sum1 += int(i)

for i in x[1:]:
    for j in i.split('+'):
        sum1 -= int(j)

print(sum1)




