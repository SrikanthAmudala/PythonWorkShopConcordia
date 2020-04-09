class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        temp = set()
        while True:
            count+=1
            n = sum_sq_num(n)
            if n == 1:
                return True

            else:
                if n in temp:
                    return False
                else:
                    temp.add(n)

def sum_sq_num(num):
    sum_n = 0
    while num % 10 != 0 or num//10!=0:
        rem = num % 10
        num = num // 10
        sum_n += rem ** 2
    return sum_n

x = Solution()
x.isHappy(5)