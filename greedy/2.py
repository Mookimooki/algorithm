
def recursive_sum(strCtn, flag, idx, dir):
    if idx > len(strCtn):
        idx = idx - len(strCtn)
    elif idx < 0:
        idx = idx + len(strCtn)
        
    if flag[idx] > 1:
        return
    
    flag[idx] += 1
    temp1 = 0
    temp2 = 0
    
    if dir != 'left':
        temp1 = recursive_sum(flag, idx + 1, 'right')
    if dir != 'right':
        temp2 = recursive_sum(flag, idx - 1, 'left')
        
    

def solution(name):
    strCtn = list(map(lambda x: min(ord(x)-65, 91-ord(x)), name))
    if min(strCtn) > 0:
        return sum(strCtn) + len(strCtn) - 1 
    return recursive_sum(strCtn, [0]*len(name), 0, 'all')

print(solution("JAZ"))
