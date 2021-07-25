#https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answer = []
    for arr in commands:
        temp = array[arr[0]-1: arr[1]].sort()
        answer.append(temp[arr[2]-1])
    return answer

if __name__ == "__main__":
	solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]);