def solution(s):
    stack = []
    for a in s:
        if a is '(':
            stack.append(a)
        else: # ')'
            if stack:
                stack.pop()
            else:
                return False
        
    return not stack