#Single Number
#问题描述
#Given an array of integers, every element appears twice except for one. Find that single one.
#找出两两重复的数组中单身的一个
#我的做法:先排序，两两比较大小，不相等的即为单个
#最快方法：异或

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