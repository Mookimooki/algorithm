def solution(citations):
    citations.sort(reverse= True)
    temp = None
    for i, val in enumerate(citations, 1):
        if i <= val: temp = i
    return temp

if __name__ == "__main__":
	print(solution([1]))