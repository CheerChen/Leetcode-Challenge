#Single Number & Single Number II
#问题描述
#Given an array of integers, every element appears twice except for one. Find that single one.
#找出两两重复或三次重复的数组中单独的一个
#我的做法:先排序，比较大小，不相等的即为单个，还是这个方法好，稍加改造就能用于三重复的
#两两重复最快方法：异或

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if len(A)==1:
            return A[0]
        else:
            A=sorted(A)
            l=len(A)
            i=0
            while i<l:
                if i<l-1 and A[i]==A[i+1]:
                    i=i+2
                else:
                    return A[i]
    # @param A, a list of integer
    # @return an integer
    # 60ms
    def singleNumber2(self, A):
        if len(A)<3:
            return A[0]
        else:
            A=sorted(A)
            l=len(A)
            i=0
            while i<l:
                if i<l-2 and A[i]==A[i+1] and A[i]==A[i+2]:
                    i=i+3
                else:
                    return A[i] 

a=Solution()
print a.singleNumber2([1,0,0,0,1])