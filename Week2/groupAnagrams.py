strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

strs = ["eat","tea","tan","ate","nat","bat"]


def string_combinations(item):
    temp = []
    if item == "":
        return [""]
    
    for i in range(len(item)):
        item = item[1:] + item[0]
        temp.append(item)
    return temp


def anagrams(strs):
    final_list = []
    for i in strs:
        all_comb = string_combinations(i)
        if all_comb[0]=="":
            all_comb = ["" for _ in range(strs.count(""))]
        temp = []
        for j in all_comb:
            if j in strs:
                temp.append(j)
                strs.remove(j)
        final_list.append(temp)

    for i in strs:
        final_list.append([i])
    return final_list


# strs = ["", "", "n"]
print(anagrams(strs))

# for i in strs:
# 	for j in strs:


# # strs = ["eat", ["tea", "tan"], ["ate", "nat", "bat"]]

# # strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
# anagrams = []

# strs = ["dad","day","",""]

# for i in range(len(strs)):
# 	if strs[i] not in [j for i in anagrams if len(i) > 0 for j in i]:
# 		temp = [strs[i]]
# 		for nextWord in range(i+1, len(strs)):
# 			count = 0
# 			currentWord = [i for i in strs[i]]
# 			nextWord_ = [i for i in strs[nextWord]]
# 			for char in strs[i]:	
# 				if char in nextWord_:
# 					count+=1
# 					currentWord.remove(char)
# 					nextWord_.remove(char)

# 			if count==len(strs[nextWord]) and count==len(strs[i]):
# 				if currentWord==nextWord_:
# 					temp.append(strs[nextWord])


# 		anagrams.append(temp)

# print(anagrams)


# anagrams = [value for (key, value) in anagrams.items()]
# print(anagrams)
