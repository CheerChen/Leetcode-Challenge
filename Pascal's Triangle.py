#Pascal's Triangle I&II
#问题描述
#Given numRows, generate the first numRows of Pascal's triangle.
#生成帕斯卡三角
#Given an index k, return the kth row of the Pascal's triangle.
#获取第k+1行的序列
#思路:前后补0做前后加法生成下一行

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        loopList=[]
        ret=[]
        for x in range(numRows):
            loopList=self.nextRow(loopList)
            ret.append(loopList)
        return ret

    # @return a list of integers
    def getRow(self, rowIndex):
        ret=[]
        for x in range(rowIndex+1):
            ret=self.nextRow(ret)
        return ret

    def nextRow(self,lists):
        if len(lists)==0:
            return [1]
        lists.append(0)
        lists.insert(0,0)
        nextLists=[]
        for x in range(len(lists)):
            if x>0:
                nextLists.append(lists[x]+lists[x-1])
        del lists[0]
        del lists[-1]
        return nextLists

a=Solution()
print a.generate(2)
print a.getRow(0)