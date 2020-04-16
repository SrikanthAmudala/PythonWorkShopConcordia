nums = [ -1, 1, 3, -2, 4, 5, -3, 1]

max_at_index = max_value = nums[0]
for i in range(1, len(nums)):
    max_at_index = max(nums[i], max_at_index + nums[i])
    if max_at_index > max_value:
        max_value = max_at_index
print(max_value)