import sys
input = sys.stdin.readline

l = int(input())
s = input().strip()
hash_val = 0
for idx, char in enumerate(s):
    hash_val += (ord(char)-ord("a")+1) * 31 ** idx

print(hash_val % 1234567891)