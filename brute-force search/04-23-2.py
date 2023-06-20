# https://school.programmers.co.kr/learn/courses/30/lessons/87946
maxCount = 0

def solution(k, dungeons):
    trace(k, dungeons, 0)
    global maxCount
    return maxCount

def trace(k, dungeons, count):
    print('######', k, dungeons, count)
    global maxCount
    maxCount = max(maxCount, count)
    for dungeon in dungeons:
        if(k >= dungeon[0]):
            temp = dungeons[:]
            temp.remove(dungeon)
            trace(k - dungeon[1], temp, count + 1)

print(solution(80, [[80,20],[50,40],[30,10]]))