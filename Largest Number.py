#Largest Number
#问题描述
#Given a list of non negative integers, arrange them such that they form the largest number.
#得到一个列表中的数字所能组合成的最大数字
#思路:自定义比较函数，逐个字符对比，位数不够就拼自己再做对比
#注意得到结果要先转成数字
#用全排列肯定慢啊

class Solution:
    # @param num, a list of integers
    # @return a string
    #57ms
    def largestNumber(self, num):
        strs=map(str,num)
        if len(strs)>1:
            strs.sort(self.compare,reverse = True)
        
        ret=int(''.join(strs))
        return str(ret)

    def compare(self,x,y):
        p=0
        while True:
            if p==len(x):
                x+=x
            if p==len(y):
                y+=y
            if x==y:
                return 0
            if x[p]>y[p]:
                return 1
            elif x[p]==y[p]:
                p+=1
            else:
                return -1


    # Memory Limit Exceeded
    def largestNumberSlow(self, num):
        strs=map(str,num)
        if len(num)>1:
            strs=sorted(strs,reverse=True)
            ret=''
            lstack=[]
            for x in range(len(strs)):
                    if x>0:
                        # prefix=self.commonPrefix(strs[x],strs[x-1])
                        # print prefix
                        if strs[x][0:1]==strs[x-1][0:1]:
                            if x==1:
                                lstack.append(strs[x-1])
                            lstack.append(strs[x])
                        else:
                            if len(lstack)>0:
                                # print lstack
                                ret+=self.findLargest(lstack)
                                lstack=[]
            if len(lstack)>0:
                ret+=self.findLargest(lstack)
                lstack=[]
            strs=[ret]

        return ''.join(strs)
        
    def perm(self,l):
        if(len(l)<=1):
            return [l]
        r=[]
        for i in range(len(l)):
            s=l[:i]+l[i+1:]
            p=self.perm(s)
            for x in p:
                r.append(l[i:i+1]+x)
        return r

    def findLargest(self,lstack):
        ret=self.perm(lstack)
        temp=[]
        for x in ret:
            temp.append(''.join(map(str,x)))
        return str(max(map(int,temp)))

        
a=Solution()
print a.largestNumber([12,123,1212])