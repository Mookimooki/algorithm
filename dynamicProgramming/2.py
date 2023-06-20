#https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    for row in range(len(triangle)-2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row+1][col], triangle[row+1][col+1])
    return triangle[0][0]

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) #30