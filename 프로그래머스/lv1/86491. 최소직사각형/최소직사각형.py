def solution(sizes):
    
    for size in sizes:
        size.sort()     # 앞에 작은 거, 뒤에 큰 거.
        
    w = 1
    h = 1
    for size in sizes:
        w = max(w, size[0]) # 작은 거 중에 젤 큰 거
        h = max(h, size[1]) # 큰 거 중에 젤 큰거.
    
    return w * h