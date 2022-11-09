def solution(s):
    count = [0, 0]
    
    while s != '1':
        count[1] += s.count('0')
        s = format(len(s.replace('0', '')), 'b')
        count[0] += 1

    return count