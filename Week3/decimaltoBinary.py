"""
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
num >= 1
You could assume no leading zero bit in the integer’s binary representation.

"""

def decimalToBinary(n):
	if n == 0:
		return 0
	if n==1:
		return 1

	binaryStr = ""
	while n>=1:
		rem = n%2	
		n = n//2 
		# binaryStr= rem +binaryStr*10
		binaryStr= str(rem) +binaryStr
	return int(binaryStr)

def decimalToComplimentBinary(n):
	if n == 0:
		return 1
	if n==1:
		return 0
	if n==2:
		return 1
	binaryStr = ""
	decimal = 0
	count=0
	while n>=1:
		rem = n%2	
		n = n//2 
		if rem==0:
			rem =1
		elif rem==1:
			rem = 0
		# binaryStr= rem +binaryStr*10
		binaryStr= str(rem) +binaryStr
		decimal += rem * 2**count
		count+=1
	return int(binaryStr)

def decimalToComplimentDecimal(n):
	"""
	Efficient way
	"""
	if n == 0:
		return 1
	if n==1:
		return 0
	if n==2:
		return 1
	decimal = 0
	count=0
	while n>=1:
		rem = n%2	
		n = n//2 
		if rem==0:
			rem =1
		elif rem==1:
			rem = 0
		
		decimal += rem * 2**count
		count+=1
	return decimal

def binaryToDecimal(n):
	decimal = 0
	count=0
	if n ==0:
		return 0

	while n>0:
		rem = n%10
		n = n//10
		decimal += rem * 2**count
		count+=1
	return decimal

	
n = 6
binary = decimalToBinary(n)
complimentBinary = decimalToComplimentBinary(n)

print("Binary: ",binary)
print("Compliment",complimentBinary)
complimentDecimal = binaryToDecimal(complimentBinary)
print("complimentDecimal: ",complimentDecimal)


# efficeint answer:
print("complimentDecimal: ", decimalToComplimentDecimal(n))




