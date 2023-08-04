def distance(c, stables, minimum):
    prev = stables[0]
    c -= 1
    for i in range(1, len(stables)):
        if stables[i] - prev >= minimum: 
            prev = stables[i]
            c -= 1
            if c == 0: return minimum
    return minimum - 1

# n, c = map(int, input().split())
# stables = list(map(int, input().split()))

n, c = 5, 3
stables = [1, 2, 8, 4, 9]

stables.sort()
lt, rt = 1, stables[-1]

answer = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if distance(c, stables, mid) >= mid:
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1
    
print(answer)