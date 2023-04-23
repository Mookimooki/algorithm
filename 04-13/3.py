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

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
