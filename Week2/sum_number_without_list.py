# [1,9,9] -> [2,0,0]

# [9,9,9] -> [1,0,0,0]


def sum_of_list(x):
	carry = 1
	for i in range(len(x)-1, -1, -1):
		digit = x[i] + carry
		if digit == 10:
			carry = 1
		else:
			carry = 0
		x[i] = digit%10

	if carry == 1:
		return [1]+x
	return x


x = [1,0]
print(sum_of_list(x))
