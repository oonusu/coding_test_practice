def solution(n):
    
    x_2 = [0]
    x = 1
    for i in range(n-1):
        x_2.append(x)
        x = x_2[0] + x
        x_2.pop(0)
        
    return x % 1234567