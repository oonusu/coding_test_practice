def solution(n):
    count = 1
    
    for i in range(1, n // 2 + 1):
        x = i
        a = 1
        while x < n:
            x += i + a
            a += 1
        if x == n:
            count += 1
            
    return count