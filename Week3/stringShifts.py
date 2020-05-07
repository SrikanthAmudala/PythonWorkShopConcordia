"""
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.


Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

PNP

-> hard ware upstraction layer

"""

s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]

# 0-> first element to last
# 1-> last element to first

for shif in shift:
	if shif[0]==0:
		s = s[shif[-1]:] + s[:shif[-1]] # s[1:] = bca
	else:
		s = s[len(s) - shif[-1]:] + s[:len(s) -shif[-1]] # s[3 -2 = 1:] + s[:3-2 =1]= cab  

print(s)