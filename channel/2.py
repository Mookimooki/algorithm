def solution(n, m, k, acts): #n행, m열
    answer = [0 for _ in range(k+1)]
    filled = {
        'row': set(),
        'col': set()
    }
    
    for i in range(len(acts)-1, -1, -1):
        type, x, p = acts[i]
        if type == 1: # 행 칠하기
            if x not in filled['row']:
                answer[p] += m - len(filled['col'])
                filled['row'].add(x)
        else:  # 열 칠하기
            if x not in filled['col']:
                answer[p] += n - len(filled['row'])
                filled['col'].add(x)
    
    return answer[1:]

# print(solution(3, 4, 3, [[1,1,2],[1,2,3],[2,4,2]]), [0, 6, 3])
# print(solution(3, 3, 6, [[2, 3, 4],[1, 1, 1],[1, 2, 5],[1, 3, 5],[2, 1, 2],[2, 3, 3],]), [1, 3, 3, 0, 2, 0])
print(solution(1, 1, 2, [[1,1,1],[1,1,2]]), [0,1])