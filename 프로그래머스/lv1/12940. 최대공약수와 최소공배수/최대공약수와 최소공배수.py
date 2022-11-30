def solution(n, m):
    answer = []
    if n > m:
        n, m = m, n
    gcd = 1
    for x in range(2, n+1):
        if n % x == 0 and m % x == 0:
            gcd = max(gcd, x)
            
    lcm = n * m
    for y in range(n, n*m):
        if y % n == 0 and y % m == 0:
            lcm = y
            break
    answer.append(gcd)
    answer.append(lcm)
    return answer