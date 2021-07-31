from collections import defaultdict

def solution(genres, plays):
    answer = []
    counter = defaultdict(list)
        
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in counter:
            counter[genre].append(0) 
        counter[genre][0] += play
        counter[genre].append((idx, play)) 
    genreSorted = sorted(counter.items(), key = lambda x: -x[1][0])
    
    for genre, songs in genreSorted:
        songs = sorted(songs[1:], key = lambda x: -x[1])
        answer.extend([x for x,y in songs[:2]])
        
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]))