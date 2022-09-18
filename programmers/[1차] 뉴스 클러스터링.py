from collections import defaultdict


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1Dict = defaultdict(int)
    str2Dict = defaultdict(int)

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1Dict[str1[i] + str1[i + 1]] += 1

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2Dict[str2[i] + str2[i + 1]] += 1

    _max = {}
    _min = {}

    for key, val in str1Dict.items():
        if key in _max:
            _max[key] = max(_max[key], val)
        else:
            _max[key] = val

        if key in _min:
            _min[key] = min(_min[key], val)
        else:
            _min[key] = val

    for key, val in str2Dict.items():
        if key in _max:
            _max[key] = max(_max[key], val)
        else:
            _max[key] = val

        if key in _min:
            _min[key] = min(_min[key], val)
        else:
            _min[key] = val

    total = 0
    for val in _max.values():
        total += val

    interTotal = 0
    for key, val in _min.items():
        if key in str1Dict and key in str2Dict:
            interTotal += val

    if not total:
        return 65536
    print(round(65536 * (interTotal / total)))
    return round(65536 * (interTotal / total))

assert solution("FRANCE", "french") == 16384