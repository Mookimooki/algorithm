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


def solution1(cards, slot_size):
    cards.sort()
    slots = [[cards.pop(0)]]

    for card in cards:
        flag = False

        slotLen = len(slots)
        for n in range(slotLen):
            slot = slots[n]
            if card - slot[-1] == 1:
                if len(slot) < slot_size -1:
                    slot.append(card)
                else:
                    del slots[n]
                flag = True
                break

        if not flag:
            slots.append([card])

    return all(len(slot) == slot_size for slot in slots)

print(solution1([5,3,4,4], 2))
print(solution1([5,3,2,5], 2))
print(solution1([2,3,4,5], 3))

print(solution1([2,3,4,2,3,4], 3))