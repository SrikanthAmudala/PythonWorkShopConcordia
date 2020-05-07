"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

"""
hint: use prefix sufix product
"""

def productExceptSelf(nums):  
	"""
	O(n^2)
	"""
    temp = []
    for i in range(len(nums)):
        nums_prod = 1
        for j in range(len(nums)):
            if i!=j:
                nums_prod*=nums[j]
        temp.append(nums_prod)
    return temp


def productExceptSelfLinearTime(nums):
	"""
	O(n)
	"""
    prefix_prod = 1
    sufix_prod = 1
    prefix_list = []
    sufix_list = [None]*len(nums)
    
    for i in range(len(nums)):
        prefix_prod *=nums[i]       
        sufix_prod *= nums[len(nums)-1-i] 
        prefix_list.append(prefix_prod)			# [2, 6, 24]

        										# [2, 3, 4]

        										# [24, 12, 4]

        										# [12, 8, 6]

        sufix_list[len(nums)-1-i] = sufix_prod	# [24, 24, 12, 4]
        
    final_list = []
    for i in range(len(nums)):   
        if i == 0: # i = 0
            final_list.append(sufix_list[i+1])  # -1 1
        elif i == len(nums)-1:
            final_list.append(prefix_list[i-1])  # -1 1
        else:
            final_list.append(prefix_list[i-1] * sufix_list[i+1])
    return final_list
    




nums =  [1,2,3,4]
productExceptSelfLinearTime(nums)

