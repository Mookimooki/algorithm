def solution(cards, words):
    for i in range(3):
        cards[i] = alphabetCnt(cards[i])
    
    answer = []

    for word in words:
        check, flag = [False, False, False], False
        wordDict = alphabetCnt(word)
        for alphabet in wordDict:
            if flag: break
            for i in range(4):
                if i == 3: flag = True
                elif alphabet in cards[i].keys():
                    if cards[i][alphabet] >= wordDict[alphabet]:
                        check[i] = True
                    else: flag = True
                    break
            
        if not flag and False not in check:
            answer.append(word)

    if len(answer) < 1: return ['-1']
    return answer

def alphabetCnt(string):
    dict = {}
    for chr in string:
        if chr in dict: dict[chr] += 1
        else: dict[chr]= 1
    return dict

print(solution(['ABACDEFG', 'NOPQRSTU', 'HIJKLKMM'], ['GPQM', 'GPMZ', 'EFU', 'MMNA']), ['GPQM', 'MMNA'])
print(solution(['AABBCCDD', 'KKKKJJJJ', 'MOMOMOMO'], ['AAAKKKKKMMMMM','ABCDKJ']), ['-1'])