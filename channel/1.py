import math

def solution(mod1, mod2, max_range):
    return max_range // mod1 - max_range // ((mod1 * mod2) // math.gcd(mod1, mod2))


print(solution(4, 4, 20), 0)
print(solution(4, 3, 20), 4)
print(solution(4, 3, 24), 4)
print(solution(3, 4, 20), 5)