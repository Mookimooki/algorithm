from collections import Counter
from functools import reduce

def solution(clothes):
    return reduce(lambda x,y: x*(y+1), Counter([y for x,y in clothes]).values() ,+1) - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))