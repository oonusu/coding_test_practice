def solution(s):
    s = list(s.lower())
    for i, w in enumerate(s):
        if i == 0:
            if w.isalpha():
                s[i] = w.upper()
                continue
                
        if w == ' ':
            
            if i+1 < len(s) and s[i+1].isalpha():
                s[i+1] = s[i+1].upper()
            continue
        
    return ''.join(s)