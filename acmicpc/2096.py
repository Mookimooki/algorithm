#https://www.acmicpc.net/problem/2096
 
n = int(input())

maxResult = [0, 0, 0]
minResult = [0, 0, 0]

for _ in range(n):
    nums = list(map(int, input().split()))
    
    maxResult = [nums[0] + max(maxResult[0], maxResult[1]), nums[1] + max(maxResult[0], maxResult[1], maxResult[2]), nums[2] + max(maxResult[1], maxResult[2])]
    minResult = [nums[0] + min(minResult[0], minResult[1]), nums[1] + min(minResult[0], minResult[1], minResult[2]), nums[2] + min(minResult[1], minResult[2])]
        
print(max(maxResult), min(minResult))