# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    for el in sizes:
        if el[0] < el[1]:
            temp = el[1]
            el[1] = el[0]
            el[0] = temp

    maxW = 0
    maxH = 0

    for el in sizes:
        if(maxW < el[0]): maxW = el[0]
        if(maxH < el[1]): maxH = el[1]

    return maxW * maxH

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))