def solution(s):
    s = s[1:-1].split(",")
    for i,e in enumerate(s):
        s[i] = int(e.replace("{","").replace("}",""))
    str_set = set(s)
    str_list = list(str_set)
    str_list.sort(key = lambda x:s.count(x), reverse=True)
    return str_list