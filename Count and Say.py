#Count and Say
#问题描述
#The count-and-say sequence is the sequence of integers
#从1开始计数，11，21，1211，给出第n个数字
#非常有意思，练习递归
#第一，给一个数，返回一个拼写的数，
#递归返回第n个值

#关于python的递归函数，一定要有返回值，否则递归完成后给出的是None
#关于产生的序列有一些有趣的规则，比如序列中永远不会出现大于4的整数

class Solution:
    # @return a string
    def countAndSay(self, n):
        if 0 == n:
            return ''
        if 1 == n:
            return '1'
        return self.countRecursive(0,n,1)

    def countRecursive(self,x,n,ints):
        x+=1
        if x==n:
            return ints
        ints=self.say(ints)
        return self.countRecursive(x,n,ints)


    def say(self,ints):
        ret=''
        strs=str(ints)
        l=len(strs)
        count=1
        for x in range(l):
            if x+1<l and strs[x]==strs[x+1]:
                count+=1
            else:
                ret+=str(count)+strs[x]
                count=1
        return ret

a=Solution()
print a.countAndSay(40)
