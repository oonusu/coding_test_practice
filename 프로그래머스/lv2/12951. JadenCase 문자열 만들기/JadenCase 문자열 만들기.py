def solution(s):
    words = list(s.split(' '))
    answer = []

    for w in words:
        answer.append(w.capitalize())
    
    return ' '.join(answer)