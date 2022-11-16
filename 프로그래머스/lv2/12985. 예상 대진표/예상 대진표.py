def solution(n,a,b):
    answer = 0
    _round = 0
    matches = [0] * (n + 1)
    matches[a] = 1
    matches[b] = 1
    
    while len(matches) > 2:
        _round += 1
        matches = [0] * ((len(matches) - 1) // 2 + 1)
        a = (a+1) // 2
        matches[a] = 1
        b = (b+1) // 2
        matches[b] = 1
        if a == b:
            break
    
    return _round