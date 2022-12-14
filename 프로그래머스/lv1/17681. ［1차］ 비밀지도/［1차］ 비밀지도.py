def solution(n, arr1, arr2):
    answer = []
    tmp = []
    for i in range(n):
        answer.append(format(arr1[i] | arr2[i], f'{n}b'))
        answer[-1] = answer[-1].replace("1", "#").replace("0", " ")
    
    return answer