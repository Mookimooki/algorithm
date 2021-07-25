def solution(citations):
    citations.sort(reverse= True)
    temp = 0
    for i, val in enumerate(citations, 1):
        if i <= val: temp = i
    return temp

if __name__ == "__main__":
	print(solution([0,0,0]))