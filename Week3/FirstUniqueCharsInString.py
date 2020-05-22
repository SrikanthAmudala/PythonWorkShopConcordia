

def firstUniqChar(s):
	# navie approch 
	# the inbuilt function 
	for i in range(len(s)):
		if s.count(s[i])==1:
			return i

def firstUniqCharEff(s):
	# O(n)
	strMap = {}
	for i in s:
		if strMap.get(i)==None:
			strMap[i] = 1
		else:
			strMap[i]+=1
	for i in range(len(s)):
		if strMap[s[i]]==1:
			return i
	return -1

