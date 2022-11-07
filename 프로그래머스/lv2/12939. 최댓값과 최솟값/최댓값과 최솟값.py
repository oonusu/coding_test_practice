def solution(s):
    nums = list(map(int, s.split()))
    min_ = min(nums)
    max_ = max(nums)
    return str(min_) + ' '+ str(max_)