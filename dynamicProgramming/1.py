#https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    possibilities = [set() for x in range(9)]
    possibilities[1] = {N}
    possibilities[2] = {N + N, 1, N * N, 0, 10*N + N}

    if number in possibilities[1]: return 1
    if number in possibilities[2]: return 2

    for i in range(3, 9):
        possibilities[i] = {int('1' * i) * N}
        for j in range(1, i):
            for a in possibilities[j]:
                for b in possibilities[i-j]:
                    possibilities[i].add(a + b)
                    if b != 0:
                        possibilities[i].add(a // b)
                    possibilities[i].add(a * b)
                    possibilities[i].add(a - b)
                    
        if number in possibilities[i]: return i
        
    return -1

print(solution(5, 12)) #4
print(solution(2, 11)) #3