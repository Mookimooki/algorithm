def solution(blocks, distances): #len(block) < 5000, block[x] < 100,000, len(distances) == len(blocks) - 1, distances[x] < 100,000
    size = len(blocks)
    dp = {
        'right': [(1, blocks[i]) for i in range(size)],
        'left': [(1, blocks[i]) for i in range(size)],
    }
    
    for i in range(1, size):
        dist = 0
        cnt, reach = dp['left'][i][0], 0
        
        for j in range(i-1, -1, -1):
            dist += distances[j]
            if dist > blocks[i]: break
            
            if reach < dist:
                cnt += dp['left'][j][0]
                reach = dist + dp['left'][j][1]
            
        dp['left'][i] = (cnt, max(reach, blocks[i]))
        
    for i in range(size-2, 0, -1):
        dist = 0
        cnt, reach = dp['right'][i][0], 0
        
        for j in range(i, size-1):
            dist += distances[j]
            if dist > blocks[i]: break
        
            if reach < dist:
                cnt += dp['right'][j][0]
                reach = dist + dp['right'][j+1][1]
            
        dp['right'][i]= (cnt, max(reach, blocks[i]))
        
    cnt, answer = 0, 0

    while cnt < size:
        rightMax = max(dp['right'], key = lambda x: x[0])
        leftMax =  max(dp['left'], key = lambda x: x[0])
        if rightMax > leftMax:
            idx = dp['right'].index(rightMax)
            for j in range(idx, idx + rightMax[0]): dp['right'][j] = (0, 0)
            cnt += rightMax[0]
        else:
            idx = dp['left'].index(leftMax)
            for j in range(idx, idx - leftMax[0] - 1, -1): dp['left'][j] = (0, 0)
            cnt += leftMax[0] 
        answer += 1
            
    return answer
    
    

# print(solution([5, 10, 2, 7, 9, 4], [7, 1, 3, 8, 5]), 2)
# print(solution([15, 10, 9, 9, 13, 15, 8, 6, 10, 7], [11, 10, 6, 12, 6, 6, 10, 8, 8]), 4)
print(solution([10,10], [10]), 1)
print(solution([10,10], [11]), 2)
print(solution([10,2], [9]), 1)
print(solution([1, 1, 1, 1, 1, 1], [5, 5, 5, 5, 5]), 6)