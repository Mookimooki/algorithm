def solution(numbers):
    nums = sorted(list(map(str, numbers)), reverse=True, key = lambda x: x*3)
    if nums[0] == "0": return "0"
    return ''.join(nums)

if __name__ == "__main__":
	print(solution([3, 30, 34, 5, 9]))
 	# print(solution([0,0]))