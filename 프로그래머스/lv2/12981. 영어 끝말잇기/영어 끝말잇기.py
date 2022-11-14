def solution(n, words):
    count = [0] * n
    used_words = []
    last_letter = words[0][0]
    
    def turn(num_player, word):
        nonlocal last_letter
        count[num_player] += 1
        
        if word[0] != last_letter or word in used_words or len(word) == 1:
            return [num_player+1, count[num_player]]
        used_words.append(word)
        last_letter = word[-1]
        print(last_letter)
        
        
    for i, word in enumerate(words):
        # print(last_letter)
        answer = turn(i%n, word)
        # print(last_letter)
        if answer:
            return answer
        
    return [0,0]