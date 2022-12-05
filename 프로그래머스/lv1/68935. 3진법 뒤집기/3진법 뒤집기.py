def solution(n):
    answer = []
    
    rev_3 = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_3 += str(mod)
    n_3 = rev_3[::-1]
    
    stack = []
    for i in n_3:
        stack.append(i)
    while stack:
        answer.append(stack.pop())
    answer = ''.join(answer)
        
    return int(answer, 3)
