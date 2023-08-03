def count(songs, capacity):
    answer, sum = 1, 0
    for song in songs:
        sum += song
        if sum > capacity:
            sum = song
            answer += 1
    return answer
    
n, m = map(int, input().split())
songs = list(map(int, input().split()))

# n, m = 9, 3
# songs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

start, end = max(songs), sum(songs)
    
answer = 0
while start <= end:
    mid = (start + end)//2
    if count(songs, mid) <= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
