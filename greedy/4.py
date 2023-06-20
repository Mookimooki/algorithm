# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution1(people, limit):
    people.sort()
    answer = 0
    weightSum = 0
    while len(people) > 0:
        minWeight = people.pop(0)
        weightSum = minWeight
        answer += 1
        for weight in people[::-1]:
            if weightSum + weight > limit:
                continue
            else:
                people.remove(weight)
                weightSum += weight
                if limit - weightSum < minWeight:
                    weightSum = 0
                    break
    
    return answer

def solution(people, limit):
    people.sort()
    rightIdx = len(people)
    answer = 0   
    leftIdx = 0
    
    while leftIdx < rightIdx:
        minWeight = people[leftIdx]
        weightSum = minWeight
        answer += 1
        while limit >= weightSum + minWeight and leftIdx < rightIdx:
            rightIdx -= 1
            if weightSum + people[rightIdx] > limit:
                answer += 1
            else:
                weightSum = 0
                break
        leftIdx += 1
    
    return answer

print(solution([70, 50, 80, 50], 100))          #3
print(solution([100, 50, 50], 100))             #2
print(solution([70, 80, 50], 100))              #3
print(solution([50, 100, 100, 140], 200))       #2
print(solution([70, 50, 80, 50, 90, 40], 240))  #3
print(solution([100, 100, 100, 100, 100], 100))          #5

