# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    return max(0, count * (1 + count) / 2 * price - money)