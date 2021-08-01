def solution(priorities, location):
    answer = 1
    temp = [x for x in enumerate(priorities)]    

    while len(temp) > 1:
        maxTuple = max(enumerate(temp), key = lambda x : x[1][1])
        if maxTuple[1][0] == location:
            break
        answer += 1
        temp = temp[maxTuple[0]+1:] + temp[:maxTuple[0]]        
        
    return answer

print(solution([1,2,9,9,1,2,2], 4))