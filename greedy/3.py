import sys
sys.setrecursionlimit(10**6)

def solution(number, k):
    for idx, x in sorted(enumerate(number), key = lambda x: (x[1], -x[0]), reverse=True):
        if(idx <= k):
            if k == 0:
                return number
            elif len(number) < idx + k + 1:
                return x
            else:
                return x + solution(number[idx+1:], k - idx)

print(solution("1231234", 3))