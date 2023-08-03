def distance(c, stables, minimum):
    prev = 0
    c -= 1
    for i in range(1, len(stables)):
        if stables[i] - prev >= minimum: 
            prev = stables[i]
            c -= 1
            if c == 0: return minimum
    return minimum - 1

n, c = map(int, input().split())
stables = list(map(int, input().split()))

stables.sort()
lt, rt = 1, max(stables)

answer = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if distance(c, stables, mid) >= mid:
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1
    
print(answer)