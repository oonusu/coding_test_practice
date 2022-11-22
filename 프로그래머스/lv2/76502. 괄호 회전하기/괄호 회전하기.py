def solution(s):
    answer = 0
    
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        stack = []
        
        for j in tmp:
            if not stack:
                if j == ')' or j == '}' or j== ']':
                    break
                else:
                    stack.append(j)
            else:
                if j == ')':
                    if stack[-1] != '(':
                        break
                elif j == '}':
                    if stack[-1] != '{':
                        break
                elif j == ']':
                    if stack[-1] != '[':
                        break
                else:
                    stack.append(j)
                    continue
                stack.pop()
        else:
            print(stack)
            if not stack:
                answer += 1
            
    return answer