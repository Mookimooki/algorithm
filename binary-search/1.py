#https://school.programmers.co.kr/learn/courses/30/lessons/43238

def check(times, answer):
    return sum(map(lambda x: answer // x, times))

def solution(n, times):   
    lt, rt = 1, max(times) * n // len(times)
    
    answer = 0
    while lt <= rt:
        mid = (lt + rt)//2
        if check(times, mid) >= n:
            answer = mid
            rt = mid - 1
        else:
            lt = mid + 1
    return answer

print(solution(6, [7, 10]), 28)