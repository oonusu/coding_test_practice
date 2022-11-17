from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if city not in cache:
            cache.appendleft(city)
            answer += 5
            if len(cache) > cacheSize:
                cache.pop()
        else:
            cache.remove(city)
            cache.appendleft(city)
            answer += 1
        
    return answer