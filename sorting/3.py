def solution(citations):
    return max(map(min, enumerate(sorted(citations, reverse=True), 1)))

if __name__ == "__main__":
	print(solution([3, 0, 6, 1, 5]	))