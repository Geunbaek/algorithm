def solution(numbers):
    numbers.sort(key = lambda x: str(x) * 3, reverse=True)
    ans = "".join(map(str, numbers))
    return str(int(ans)) if ans else ans