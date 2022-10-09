import re;i = input;n = int(i());arr = i().split()
arr.sort(key=lambda x:(str(x)*10),reverse=True)
ans = re.sub("^0+","","".join(arr))
print(ans if ans else 0)