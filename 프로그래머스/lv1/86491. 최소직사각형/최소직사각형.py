def solution(sizes):
    answer = 0
    result = [0, 0]
    for w, h in sizes:
        if w > h:
            w, h = h, w
        result[0] = max(result[0], w)
        result[1] = max(result[1], h)
    answer = result[0] * result[1]
    return answer