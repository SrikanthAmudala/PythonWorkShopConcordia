nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

true_list = []
max_num= 0
for j in range(0, len(nums)):
    temp = [nums[j:i] for i in range(j + 1, len(nums) + 1)]
    for i in temp:
        if sum(i) > max_num:
            max_num = sum(i)
            true_list = i

