def solution(phone_book):
    phone_book.sort(key = len)
    for i, number in enumerate(phone_book):
        if number in list(map(lambda x: x[:len(number)], phone_book[i+1:])):
           return False
    return True


print(solution(["123","456","789"]))