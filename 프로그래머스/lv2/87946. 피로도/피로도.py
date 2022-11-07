from itertools import permutations

def solution(k, dungeons):
    idx = []
    answer = 0
    for i in permutations(dungeons):
        t = k
        count = 0
        for j in i:
            if t >= j[0]:
                t -= j[1]
                count += 1
        answer = max(count, answer)
    return answer