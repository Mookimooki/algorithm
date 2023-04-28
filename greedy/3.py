#https://school.programmers.co.kr/learn/courses/30/lessons/42883
import itertools

def solution1(number, k):
    tt = [''.join(list(x)) for x in itertools.combinations(number, len(number) - k)]
    return max(tt);

def solution2(number, k):
    number = list(number)
    length = len(number) - k
    answer = number[-length:]
    
    for x in number[-length-1::-1]:
        if x >= answer[0]:
            changeIdx = 0
            for idx in range(len(answer)-1):
                if answer[idx] < answer[idx+1]:
                    changeIdx = idx
                    break
            answer = [x] + answer[0:changeIdx] + answer[changeIdx+1:]
                    
    return ''.join(answer)

def solution(number, k):
    number = list(number)
    length = len(number) - k
    answer = number[-length:]
    
    for x in number[-length-1::-1]:
        if x >= answer[0]:
            newNum = x
            for idx in range(len(answer)):
                if answer[idx] < newNum:
                    temp = answer[idx]
                    answer[idx] = newNum
                    newNum = temp
                elif answer[idx] == newNum:
                    continue
                else:
                    break
            
    return ''.join(answer)
    
    

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))