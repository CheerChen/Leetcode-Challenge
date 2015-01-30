#Factorial Trailing Zeroes
#问题描述
#Given an integer n, return the number of trailing zeroes in n!.
#返回阶乘结果中尾数0的个数
#做阶乘，除10计算 空间超限
#除5和5的平方数计算，对了

class Solution:
    # @return an integer
    #Memory Limit Exceeded
    def trailingZeroes1(self, n):
        ret=self.factorial(n)
        zeros=0
        while ret%10==0:
            zeros+=1
            ret=ret/10
        return zeros
    
    def factorial(self,n):
        if n==1 or n==0:
            return 1
        else:
            return self.factorial(n-1)*n
        
    #Accepted
    def trailingZeroes2(self, n):
        zeros=0
        base=5
        while n/base:
            zeros+=n/base
            base*=5
        return zeros
                
a=Solution()
print a.trailingZeroes1(100)
print a.trailingZeroes2(100)
