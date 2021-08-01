def solution(priorities, location):
    answer = 1
    mine = priorities[location]
    temp = [x for x in enumerate(priorities)]    
    
    biggerThanMine = [x for x in temp if x[1] > mine]                      
    if len(biggerThanMine) > 0:
        minAmongBigger = min(biggerThanMine, key = lambda x: (x[1], -x[0]))
        answer += len(biggerThanMine)
        temp = temp[minAmongBigger[0]:] + temp[:minAmongBigger[0]]
        
    temp = [x for x in temp if x[1] ==  mine]
    for x in temp:
        if x[0] == location:
            break;
        answer += 1
    return answer

print(solution([1,2,9,1,2,2], 3))