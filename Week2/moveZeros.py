"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

nums = [0,1,0,3,12]
nums = [0,0,1]


i = 0
count = 0
while count<len(nums):
	if nums[i] == 0:  # 0 
		nums.append(nums.pop(i))  
	else:
		i+=1
	count+=1

print(nums)