def solution(s):
    answer = ''
    string = s.split(" ", -1)
    print(string)
    for i, v in enumerate(string):
        for j, w in enumerate(v):
            if w.isalpha():
                if j % 2 == 0:
                    answer += w.upper()
                else:
                    answer += w.lower()
            else:
                answer += w
        if i + 1 < len(string):
            answer += " "
    return answer