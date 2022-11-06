def solution(string):
    my_list = []
    def fn(elem, string, my_list):
        for i, x in enumerate(string):
            tmp = string[:]
            elem.append(x)
            if elem and (elem not in my_list):
                my_list.append(''.join(elem))
            tmp = tmp[:i] + tmp[i+1:]
            fn(elem[:], tmp[:], my_list)
            elem.pop()
        return my_list

    def fn2(my_list):
        primes = []
        tmp = []
        for elem in my_list:
            if int(elem) not in tmp:
                tmp.append(int(elem))
        for num in tmp:
            if num == 0 or num == 1:
                continue
            elif num == 2:
                primes.append(2)
                continue
            else:
                for j in range(2, num):
                    if num % j != 0:
                        continue
                    else:
                        break
                else: primes.append(num)
                continue

        return primes

    fn([], string, my_list)

    return len(fn2(my_list))
