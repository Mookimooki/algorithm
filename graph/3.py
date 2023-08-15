#https://school.programmers.co.kr/learn/courses/30/lessons/49190

def solution(arrows):
    dirX = (0, 1, 1, 1, 0, -1, -1, -1)
    dirY = (-1, -1, 0, 1, 1, 1, 0 , -1)
    
    points = set()
    tempX, tempY = 0, 0
    points.add((tempX, tempY))
    answer = 0
    for arrow in arrows:
        tempX, tempY = tempX + dirX[arrow], tempY + dirY[arrow]
        temp = (tempX, tempY)
        print(temp)
        if temp in points: answer += 1
        else: points.add(temp)
    
    return answer

# print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]), 3)
print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]), 3)
# print(solution([5, 2, 7, 1, 6, 3]), 3)
# print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]), 3)
