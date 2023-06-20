#https://school.programmers.co.kr/learn/courses/30/lessons/86971

def solution(n, wires):
    for wire in wires:
        wire.sort(reverse=True)
    array = [[False] * n for _ in range(n)] 
    minDiff = 99
    for cutIdx in range(n-1):
        for wire in wires:
            array[wire[0]-1][wire[1]-1] = True
            
        selected = wires[cutIdx];
        array[selected[0] -1 ][selected[1] -1 ] = False
        queue = [selected[0] -1 ]
        for sel in queue:
            for col in range(0, sel):
                if (sel != selected[0]-1 or col != selected[1]-1 ) and array[sel][col]:
                    array[sel][col] = False
                    queue.append(col)
            for row in range(sel + 1, n):
                if (row != selected[0]-1 or sel != selected[1]-1 ) and array[row][sel]:
                    array[row][sel]= False
                    queue.append(row)
        minDiff = min(minDiff, abs(len(queue) * 2 - n))
        # print('### ', wires[cutIdx], len(queue), minDiff)
    return minDiff

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	)) # 3
print(solution(4, [[1,2],[2,3],[3,4]] )) # 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]] )) # 1

print(solution(6,  [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]] )) # 2
