#Find Peak Element
#问题描述
#A peak element is an element that is greater than its neighbors.
#获取峰值
#简单到哭泣

class Solution:
    # @param num, a list of integer
    # @return an integer
    #one-line-resolution
    def findPeakElement(self, num):
        return num.index(max(num))
       
    #54ms,any faster answer?
    def findPeakElement(self, s):
        for index in range(len(num)):
            if index>0 and num[index]>num[index-1]:
                if index+1==len(num) or num[index]>num[index+1]:
                    return index
        return 0