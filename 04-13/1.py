#https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3

def solution(nums): 
    species = {}    
    for el in nums:
        count = species.get(el, 0)
        species[el] = count + 1
             
    return min(len(species.keys()), len(nums)/2)

print(solution([3,3,3,2,2,4]))
