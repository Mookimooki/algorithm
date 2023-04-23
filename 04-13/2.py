#https://school.programmers.co.kr/learn/courses/30/lessons/12906
    
def solution(arr):
    answer = [arr[0]]
    
    for num in arr:
        lastNum = answer[-1]
        if lastNum != num:
            answer.append(num)
    
    return answer

print(solution([1,1,3,3,0,1,1]))
