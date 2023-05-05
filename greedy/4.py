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
    people.sort(reverse = True)
    answer = 0
    
    while len(people) > 0:
        minWeight = people.pop()
        weightSum = minWeight
        answer += 1

        while limit >= weightSum + minWeight and len(people) > 0:
            weight = people.pop(0)
            if weightSum + weight > limit:
                answer += 1
            else:
                weightSum += weight
                if limit < minWeight + weightSum:
                    weightSum = 0
                    break
    
    return answer

print(solution([70, 50, 80, 50], 100))  #3
print(solution([70, 80, 50], 100))      #3
# print(solution([50, 100, 100, 140, 180], 200))      #3