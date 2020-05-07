# Canonical form

arr = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagram(arr):
	anagrmDict = {}
	arr1 = ["".join(sorted(i)) for i in arr]

	for i in range(len(arr1)):
		if arr1[i] not in anagrmDict:
			anagrmDict[arr1[i]] = [arr[i]]
		else:
			anagrmDict[arr1[i]].append(arr[i])
	return anagrmDict.values()

groupAnagram(arr)

