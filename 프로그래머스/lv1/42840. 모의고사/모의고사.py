def solution(answers):
    count = [0,0,0]
    patterns = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    print(count)
    for i_p, pattern in enumerate(patterns):
        for i_a, answer in enumerate(answers):
            if pattern[i_a % len(pattern)] == answer:
                count[i_p] += 1
    return [i+1 for i,x in enumerate(count) if count[i] == max(count)]