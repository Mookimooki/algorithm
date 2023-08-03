#https://school.programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    length, wordLength = len(begin), len(words)
    q, chk = [(begin, 0)], [False for _ in range(wordLength)]
    if target not in words: return 0
    
    while len(q) > 0:
        begin, val = q.pop(0)
        if begin == target: return val
        if val > len(words): return 0
        
        for n in range(length):
            start = begin[0:n]
            end = begin[n+1:]
            
            for i in range(wordLength):
                if chk[i]: continue
                word = words[i]
                if start == word[0:n] and end == word[n+1:]:
                    chk[i] = True
                    q.append((word, val+1))

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'cog', ['cog', 'log', 'lot', 'dog', 'dot', 'hot']))
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))
print(solution('aab', 'aba', ['abb', 'aba']))
print(solution('aaa', 'abc', ['aac', 'bac', 'ccb', 'abc', 'cba', 'bbb']))
