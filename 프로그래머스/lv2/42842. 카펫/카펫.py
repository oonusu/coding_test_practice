def solution(brown, yellow):
    total = brown + yellow
    hegith = 0
    width = 0
    for i in range(3, total):
        if total % i == 0:
            print(i)
            height = i
            width = total // i
            if (height-2) * (width-2) == yellow:
                break
        
    return [width, height]
