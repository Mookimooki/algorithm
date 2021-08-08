from itertools import permutations
from math import sqrt

def solution(numbers):
    cases = set()
    for length in range(1, len(numbers) + 1):
        cases.update(permutations(numbers, length))
    cases = set(map(lambda x: int(''.join(x)), cases))
    
    maxNum = max(cases)
    primeArr = [False, False, True] + [True, False] * (maxNum // 2)    
    for i in range(2, maxNum + 1):
        if primeArr[i] == True:
            j = 2
            while i * j <= maxNum:
                primeArr[i * j] = False
                j += 1
    
    return sum([1 for x in cases if primeArr[x] == True])

print(solution("1234"))