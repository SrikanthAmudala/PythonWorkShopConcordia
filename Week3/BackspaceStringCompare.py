S = "###c#ab###fs#j"
T = "ad#c"

def stringComp(S):
	temp = []
	for i in S:
		if i=="#" and len(temp)!=0:
			temp.pop(-1)
		elif i!="#":
			temp.append(i)

	return "".join(temp)
	
print(stringComp(S))