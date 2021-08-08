def solution(answers):
    supo = [0] * 3
    supo[0] = ([1,2,3,4,5] * (len(answers) // 5 + 1))[:len(answers)]
    supo[1] = ([2,1,2,3,2,4,2,5] * (len(answers) // 8 + 1))[:len(answers)]
    supo[2] = ([3,3,1,1,2,2,4,4,5,5] * (len(answers) // 10 + 1))[:len(answers)]

    for num in range(3):
        supo[num] = len([True for right, ans in zip(answers, supo[num]) if right == ans])
    
    maxScore = max(supo)
        
    return sorted([idx + 1 for idx, num in enumerate(supo) if maxScore == num])

print(solution([1,2,3,4,5]))
