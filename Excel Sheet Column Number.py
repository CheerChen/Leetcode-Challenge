#Excel Sheet Column Number
#问题描述
#Given a column title as appear in an Excel sheet, return its corresponding column number.
#Excel标题转换为数字
#思路:类似进制转换

class Solution:
    # @return an integer
    def titleToNumber(self, s):
        ret=0
        while len(s)>0:
            ret+=(ord(s[0:1])-64)*(26**(len(s)-1))
            s=s[1:len(s)]
        return ret

a=Solution()
print a.titleToNumber('B');
print a.titleToNumber('AA');
print a.titleToNumber('');