"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""

def findMaxLength(nums):
	for i in range(0, len(nums)):
		if nums[i]==0:
			nums[i] = -1


	temp = [0]
	sum_n = 0


	for i in nums:
		sum_n+=i
		temp.append(sum_n)
	print(temp)


	hash_index = {}
	max_count = 0
	
	for i in range(0, len(temp)):
		if temp[i] not in hash_index.keys():
			hash_index[temp[i]] = [i, 0]  
		else:
			hash_index[temp[i]][-1] = i - hash_index[temp[i]][0] 
			if i - hash_index[temp[i]][0] > max_count:
				max_count = i - hash_index[temp[i]][0]

	return max_count


nums = [0,0,1,0,0,1,0,0,0]




print(findMaxLength(nums))


