# O(n)

nums = [0,1,1,0,0,1,1]
  # 0 -1 0 1 0 -1 0 1

hash_map = {0:[0,0]} # init my inital index starting with 0
sum_ele = 0
max_len = 0

for i in range(0, len(nums)):
	if nums[i] == 0:
		sum_ele += -1		
	else:
		sum_ele+=1

	if hash_map.get(sum_ele)==None:
		hash_map[sum_ele] = [0, i+1] # after init my first element index becomes i+1, making index 0->1
	else:
		hash_map[sum_ele][0] = i+1-hash_map[sum_ele][-1] # i has only true index, change it to i+1 as we have 0 in front
		if hash_map[sum_ele][0] > max_len:
			max_len = hash_map[sum_ele][0]

print(max_len)