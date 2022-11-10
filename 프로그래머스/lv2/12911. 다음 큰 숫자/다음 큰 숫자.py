def solution(n):
    next = n + 1
    while format(next, 'b').count('1') != format(n, 'b').count('1'):
        next += 1
    return next