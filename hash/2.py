import collections

def solution(phone_book):
    temp = {}
    for length in set(map(len, phone_book)):
       temp[length] = collections.Counter(map(lambda x: x[:length], phone_book))
       
    for num in phone_book:
        if temp[len(num)][num] > 1: return False
    else: 
        return True


print(solution(["123","456","789"]))