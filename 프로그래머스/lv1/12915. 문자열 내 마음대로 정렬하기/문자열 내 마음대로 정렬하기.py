def solution(strings, n):
    strings.sort()  # 사전순 정렬
    strings.sort(key=lambda x:x[n])  # n번째 글자 기준 정렬
    return strings