def getLeastRecentlyUsed(cache):
    return min(cache.items(), key = lambda x: x[1])[0]

def solution(cacheSize, cities):
    if cacheSize == 0: return len(cities) * 5
    answer = 0
    cache = {}

    for index, city in enumerate(cities):
        city = city.lower()
        if city in cache:
            cache[city] = index
            answer += 1
        else:
            if len(cache) >= cacheSize:
                leastRecentlyUsed = getLeastRecentlyUsed(cache)
                del cache[leastRecentlyUsed]

            cache[city] = index
            answer += 5
    return answer

assert solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 50
assert solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) == 21
assert solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16