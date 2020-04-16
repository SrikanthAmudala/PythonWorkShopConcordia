def maxSubArray(nums):        
    max_element = nums[0]
    for i in range(0, len(nums)):
        temp = 0
        for j in range(i, len(nums)):
            temp += nums[j]
            if temp > max_element:
                max_element = temp


    return max_element

nums = [ -1, 1, 3, -2, 4, 5, -3, 1]
print(maxSubArray(nums))