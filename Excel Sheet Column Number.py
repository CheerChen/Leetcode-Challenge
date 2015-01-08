#Excel Sheet Column Number
#问题描述
#Given a column title as appear in an Excel sheet, return its corresponding column number.
#Excel标题转换为数字
#数字转换为Excel标题
#1思路:类似进制转换
#1思路:注意处理能被26整除的情况

class Solution:
    # @return an integer
    def titleToNumber(self, s):
        ret=0
        while len(s)>0:
            ret+=(ord(s[0:1])-64)*(26**(len(s)-1))
            s=s[1:len(s)]
        return ret
    # @return a string
    def convertToTitle(self, num):
        ret=''
        if num>0:
            while num>26:
                ret+=num%26 and chr(num%26+64) or chr(26+64)
                num=num%26 and num/26 or num/26-1
            ret+=num%26 and chr(num%26+64) or chr(26+64)
            ret=ret[::-1]
        return ret

a=Solution()
print a.titleToNumber('B');
print a.titleToNumber('AA');
print a.titleToNumber('');
print a.convertToTitle(52);
print a.convertToTitle(26);