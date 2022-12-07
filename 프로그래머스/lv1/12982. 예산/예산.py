def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    while budget and d:
        budget -= d.pop()
        if budget >= 0:
            answer += 1
    return answer