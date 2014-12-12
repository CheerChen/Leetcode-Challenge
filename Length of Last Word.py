#Length of Last Word
#问题描述
#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#最后一个单词个数
#思路:脚本语言大多内置数组拆分函数. 分数组,取最后一个
#正向,反向遍历字符

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        a=s.split()
        return len(a[-1])

    def lengthOfLastWord2(self, s):
        l=0
        for k,v in enumerate(s):
            if (s[k-1] is ' ') and (v is not ' '):
                l=1
            elif v is not ' ':
                l+=1
        return l

    def lengthOfLastWordBad3(self, s):
        s=s[::-1]
        l=0
        sl=len(s)
        for k,v in enumerate(s):
            if v is not ' ':
                l+=1
                if k+1<sl and s[k+1] is ' ':
                    break
        return l

a=Solution()
print a.lengthOfLastWord('  a  bbb  ')