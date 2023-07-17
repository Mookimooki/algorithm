from bisect import bisect_left

def solution(cards, slotSize):
    if len(cards) % slotSize > 0: return False
    
    cards.sort()
    
    count = 0
    while len(cards) > 0:
        if count == slotSize or count == 0:
            selected = cards.pop(0)    
            count = 1
            
        selected = selected + 1 
        if inCards(selected, cards):
            count = count + 1
            cards.remove(selected)
        else:
            return False
    
    return True

def inCards(n, cards):
    idx = bisect_left(cards, n)
    return idx < len(cards) and cards[idx] == n
    # for card in cards:
    #     if n == card: return True
    #     elif n > card: continue
    #     else: return False


print(solution([5,3,4,4], 2))
print(solution([5,3,2,5], 2))
print(solution([2,3,4,5], 3))

print(solution([2,3,4,2,3,4], 3))