from collections import defaultdict

def solution(table, languages, preference):
    t = defaultdict(list)
    scores = defaultdict(int)
    
    for el in table:
        el = el.split()
        t[el[0]] = list(reversed(el[1:]))

    for key in t.keys():
        score = 0
        for language, prefer in zip(languages, preference):
            idx = t[key].index(language) + 1 if language in t[key] else 0
            score += (idx) * prefer

        scores[key] = score    
    
    answer = sorted(scores.items(), key = lambda x : (-x[1], x[0]))[0][0]
    return answer