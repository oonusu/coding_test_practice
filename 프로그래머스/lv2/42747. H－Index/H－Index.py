def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i, e in enumerate(citations):
        if e >= i+1:
            answer = i+1
        else:
            break
    return answer