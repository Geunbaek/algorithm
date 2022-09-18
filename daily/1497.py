from re import L
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = []
max_ = 0
ans = -1

for _ in range(n):
  g, s  = input().split()
  temp = 0
  for i in range(len(s)):
    if (s[i] == "Y"):
      temp |= 1 << i
  info.append((g, temp))

def bit_counting(bit):
  ret = 0;
  while bit:
    ret += bit & 1
    bit >>= 1
  return ret

def recur(cnt, depth, state):
  global max_, ans
  now = bit_counting(state)
  if now > max_:
    max_ = now
    ans = cnt
  elif now == max_ :
    ans = min(ans, cnt)

  if depth == n: return

  recur(cnt + 1, depth + 1, state | info[depth][1])
  recur(cnt, depth + 1, state)

recur(0, 0, 0)
print(ans)