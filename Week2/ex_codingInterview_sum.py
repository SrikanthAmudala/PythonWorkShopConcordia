
def sum_of_list(x):
	digit = 0
	for i in x:
		digit = 10 *  digit + i
	digit+=1
	temp = [] 

	while digit>0:
		temp.append(digit%10)
		digit=digit//10
	
	return [temp[i] for i in range(len(temp)-1, -1, -1)]


x = [1,9,9]
print(sum_of_list(x))
