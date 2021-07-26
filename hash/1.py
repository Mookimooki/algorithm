def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for idx, val in enumerate(completion):
        if val != participant[idx]: return participant[idx]
    else:
        return participant[-1]


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))