#https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    
    if s[0] != '(':
        return False
    
    stack = []
    try:
        for parenthesis in s:
            if parenthesis != '(':
                if stack.pop() != '(':
                    return False
            else:
                stack.append(parenthesis)
        if len(stack) > 0:
            return False
    except:
        return False
        
    return True

def solution2(s):
    pair = 0
    for x in s:
        if pair < 0: break
        pair = pair + 1 if x == "(" else pair - 1
    return pair == 0


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
