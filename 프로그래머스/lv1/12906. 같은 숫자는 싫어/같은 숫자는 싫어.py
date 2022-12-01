def solution(arr):
    answer = []
    for i, v in enumerate(arr):
        if i > 0:
            if v == answer[-1]:
                continue
        answer.append(v)
                
    return answer