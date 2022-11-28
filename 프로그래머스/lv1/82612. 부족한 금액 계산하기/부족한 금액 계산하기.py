def solution(price, money, count):
    x = 0
    total = 0
    while count:
        x += 1
        total += price * x
        count -= 1
    if total < money:
        return 0
    
    return total - money